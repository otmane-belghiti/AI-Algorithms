<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=D97757&height=200&section=header&text=AI%20Algorithms&fontSize=42&fontColor=ffffff&fontAlignY=35&desc=Machine%20Learning%20-%20LLMs%20-%20AI%20Agents%20-%20AI%20Automation&descAlignY=55&descSize=18&animation=fadeIn" width="100%"/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=3000&pause=800&color=D97757&center=true&vCenter=true&width=700&lines=Supervised+%C2%B7+Unsupervised+Learning;LLM-Powered+AI+Agents;AI+Automation+%C2%B7+Applied+Machine+Learning.)](https://git.io/typing-svg)

<br/>

![Python](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/Focus-Artificial%20Intelligence-D97757?style=for-the-badge&logo=openai&logoColor=white)
![LLM](https://img.shields.io/badge/LLM-Agents%20%26%20Automation-4285F4?style=for-the-badge&logo=googlegemini&logoColor=white)
![Level](https://img.shields.io/badge/Level-Learning%20%2F%20Practice-FBBC05?style=for-the-badge&logo=google&logoColor=black)

<br/>

![Status](https://img.shields.io/badge/Status-Work%20in%20Progress-34A853?style=flat-square&logo=checkmarx&logoColor=white)
&nbsp;
![Author](https://img.shields.io/badge/Author-BELGHITI%20Otmane-D97757?style=flat-square&logo=github&logoColor=white)

</div>

---

## ◈ About This Repository

**AI-Algorithms** is my personal sandbox for learning and building across the AI stack — from classic machine learning algorithms implemented from scratch, to LLM-powered AI agents, to small AI automation workflows. It's a living repository: expect it to keep growing as I explore new algorithms, agent patterns, and automation ideas.

```yaml
repo      : AI-Algorithms
language  : Python
themes    : Machine Learning · AI Agents · LLMs · AI Automation
structure : algorithms (scripts) + AI Agents (agent experiments)
goal      : Build practical, hands-on understanding of AI end to end
```

---

## ◈ Repository Structure

| Path | Contents |
|---|---|
| `AI Agents/` | Experiments and scripts exploring LLM-powered AI agents and automated workflows |
| `K-Nearest Neighbors (KNN) - Supervised Learning.py` | KNN classifier implementation — supervised learning |
| `K-means - Unsupervised Learning.py` | K-means clustering implementation — unsupervised learning |

---

## ◈ Machine Learning Algorithms

<details>
<summary><b>View Key Concepts</b></summary>

<br/>

**Supervised vs. Unsupervised Learning**

| Type | Description | Example in This Repo |
|---|---|---|
| Supervised | Learns from labeled data to predict an outcome | K-Nearest Neighbors (KNN) |
| Unsupervised | Finds structure in unlabeled data | K-Means Clustering |

**K-Nearest Neighbors (KNN)**
A supervised classification algorithm that predicts a data point's label based on the majority label among its *k* closest neighbors in feature space.

```python
# Simplified KNN idea
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

**K-Means Clustering**
An unsupervised algorithm that partitions data into *k* clusters by iteratively assigning points to the nearest centroid and recalculating centroids.

```python
# Simplified K-Means idea
from sklearn.cluster import KMeans

model = KMeans(n_clusters=3, random_state=42)
model.fit(X)
labels = model.labels_
```

**Key Skills Practiced**
- Implementing core ML algorithms rather than only calling library APIs
- Understanding the supervised/unsupervised distinction in practice
- Evaluating model behavior on real datasets

</details>

---

## ◈ AI Agents & LLM Automation

<details>
<summary><b>View Key Concepts</b></summary>

<br/>

The `AI Agents/` folder is where classic algorithms give way to **LLM-driven systems** — code that uses a language model not just to predict a label, but to reason, plan, and act.

**What "AI Agents" Means Here**

| Concept | Description |
|---|---|
| LLM as Reasoning Engine | Using a large language model to interpret a task and decide next steps |
| Tool Use / Automation | Connecting an LLM to functions, APIs, or scripts so it can take real actions |
| Agentic Loops | Plan → Act → Observe → Refine, repeated until the task is done |
| Prompting | Structuring inputs so the LLM behaves reliably and predictably |

**Why Pair This with Classic ML**
Classic algorithms like KNN and K-Means teach the *fundamentals* of how models learn from data. AI agent experiments build on top of that foundation to explore how LLMs can automate multi-step, real-world tasks — the next layer of the AI stack.

**Key Skills Practiced**
- Designing prompts and workflows for LLM-based agents
- Structuring AI automation around clear, testable steps
- Bridging traditional ML intuition with modern LLM-driven systems

</details>

---

## ◈ Tech & Concepts Covered

<div align="center">

![Machine Learning](https://img.shields.io/badge/Machine-Learning-3776AB?style=flat-square&logo=scikitlearn&logoColor=white)
![Supervised Learning](https://img.shields.io/badge/Supervised-Learning-4285F4?style=flat-square&logo=python&logoColor=white)
![Unsupervised Learning](https://img.shields.io/badge/Unsupervised-Learning-34A853?style=flat-square&logo=python&logoColor=white)
![LLM](https://img.shields.io/badge/LLM-Large%20Language%20Models-D97757?style=flat-square&logo=openai&logoColor=white)
![AI Agents](https://img.shields.io/badge/AI-Agents-7C3AED?style=flat-square&logo=robotframework&logoColor=white)
![AI Automation](https://img.shields.io/badge/AI-Automation-EA4335?style=flat-square&logo=n8n&logoColor=white)
![Prompt Engineering](https://img.shields.io/badge/Prompt-Engineering-FBBC05?style=flat-square&logo=google&logoColor=black)

</div>

---

## ◈ Roadmap

| Status | Item |
|---|---|
| ✅ | K-Nearest Neighbors implementation |
| ✅ | K-Means clustering implementation |
| 🚧 | Expand AI Agents folder with more LLM automation examples |
| 🔜 | Add more supervised/unsupervised algorithms (e.g. Decision Trees, PCA) |
| 🔜 | Document each AI Agent script with its own mini walkthrough |

---

## ◈ Getting Started

```bash
# Clone the repository
git clone https://github.com/otmane-belghiti/AI-Algorithms.git
cd AI-Algorithms

# Install common dependencies
pip install scikit-learn numpy pandas

# Run an algorithm script
python "K-Nearest Neighbors (KNN) - Supervised Learning.py"
```

---

## ◈ Connect

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-otmane--belghiti-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/otmane-belghiti)
&nbsp;
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-D97757?style=for-the-badge&logo=netlify&logoColor=white)](https://otmane-belghiti.netlify.app)
&nbsp;
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:otmane.belghiti.officiel@gmail.com)

</div>

---

<div align="center">

*"The best way to understand AI is to build it, one algorithm at a time."*

<img src="https://capsule-render.vercel.app/api?type=waving&color=D97757&height=120&section=footer&animation=fadeIn" width="100%"/>

</div>
