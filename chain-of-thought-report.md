# Chain-of-Thought (CoT) Decoding Workflow

## **1. Introduction**

Large Language Models (LLMs) have demonstrated exceptional reasoning capabilities, often enhanced using **Chain-of-Thought (CoT) prompting**. Traditional approaches require manually crafted prompts to elicit step-by-step reasoning. However, this paper proposes an alternative—**CoT Decoding**—which **extracts reasoning paths from LLMs without explicit prompts** by modifying the decoding process.

This workflow outlines how CoT Decoding works and how it can be applied in real-world scenarios.

---

## **2. Workflow Steps**

### **Step 1: Input Question Formatting**

- The model is presented with a problem in a **standard question-answer (QA) format**.
- The question is structured such that the model is encouraged to generate an answer instead of continuing the question.

#### **Examples of the different Query:**

**Q:** I have 3 apples, my dad has 2 more apples than me, how many apples do we have in total?\
**Q:** "I bought 3 pens for $2 each and 2 notebooks for $5 each. What is the total cost?"\
**A:** *(Model calculates and provides reasoning)*

---

### **Step 2: Generating Multiple Decoding Paths**

- Instead of choosing the highest probability word (greedy decoding), **top-k alternative tokens** are considered.
- Each token leads to a different reasoning path.


#### **Deciding the best path for the reasoning:**

Suppose we have a problem mentioned below:

**Q:** "A store offers a 20% discount on a $150 item. What is the final price?"\
- **Path 1:** "The final price is $120." (incorrect)
- **Path 2:** "The discount is $30, so the final price is $120." (correct)
- **Path 3:** "Subtract 20% of $150, which is $30, from $150 to get $120." (correct, detailed reasoning)

---

### **Step 3: Evaluating Confidence in the Answer**

- Each path is assigned a **confidence score** based on token probability differences.
- Paths with **higher confidence values** (Δ) are considered more reliable.

#### **Mathematical Formula:**

\(\Delta_{k,answer} = \frac{1}{|answer|} \sum_{x_t \in answer} p(x_{1t} | x<t) - p(x_{2t} | x<t)\)


#### **Example to explain why greedy decoding won't work:**

**Q:** "A shop sells apples at $3 per kg. If you buy 5 kg, you get a 10% discount. What is the total cost?"\
- The **greedy decoding** (𝑘=0) predicted: **$15** (incorrect). there is no othe path.
- Alternative top-k paths found the correct answer: **$13.5** (high confidence Δ=0.9).


---

### **Step 4: Selecting the Best CoT Path**

- The path with the **highest confidence (Δ) is chosen** for the final response.
- Ensures logical, step-by-step reasoning.

#### **Example from the Paper:**

For the previous apple problem, the selected path was:\
- you will get per kg apple $0.3 lesser. 5 kg apple will cost you 5*($3-$0.3)=$13.5
- **Alternate Path :** "$15 - 10% of $15 = $13.50" (correct, high confidence Δ=0.9)

---

### **Step 5: Generating the Final Answer**

- The model **constructs the final response** based on the selected CoT reasoning path.
- This ensures that the **answer includes explanation** rather than just the final number.

#### **For Example**

Final Output for a profit calculation:\
"A business bought a product for $40 and sold it for $50. The profit is **$10**."

---

### **Step 6: Aggregating CoT Paths (Optional)**

- Instead of selecting a single path, multiple paths can be aggregated.
- A weighted confidence metric is used:
  \(\tilde{\Delta}_a = \sum_k \Delta_{k,a}\)



#### For a math problem, aggregating multiple paths improved accuracy by 28% over greedy decoding.

for previous problem:
**Q:** "A shop sells apples at $3 per kg. If you buy 5 kg, you get a 10% discount. What is the total cost?"\

- The **greedy decoding** (𝑘=0) predicted: **$15** (incorrect Δ=0.7).
- Alternative top-k paths found the correct answer: **$13.5** (high confidence Δ=0.9).
We can see the different of almost 30%

---

## **3. Summary & Benefits of CoT-Decoding**

### **Advantages Over Greedy Decoding:**

✅ **Does not require manual prompting**\
✅ **Extracts inherent reasoning abilities of LLMs**\
✅ **Enhances answer confidence and reliability**\
✅ **Works across multiple domains (math, finance, retail, etc.)**

---

## **4. Conclusion**

The **CoT-Decoding workflow** significantly improves the reasoning ability of LLMs **without requiring prompt engineering**. By considering alternative decoding paths and selecting those with **higher confidence**, this method reveals the model’s **intrinsic problem-solving capabilities**.
