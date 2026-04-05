# ============================================
# E-COMMERCE CUSTOMER ANALYSIS (FINAL CLEAN)
# ============================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.decomposition import PCA

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth

# ----------- TITLE -----------
st.title("E-Commerce Customer Analysis System")

# ----------- LOAD DATASET -----------
st.header("Dataset")

data = pd.read_csv("Mall_Customers.csv")
st.write(data.head())

# ----------- FEATURE SELECTION -----------
x = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# ----------- SCALING -----------
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# ----------- ELBOW METHOD -----------
st.header("Elbow Method")

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(x_scaled)
    wcss.append(kmeans.inertia_)

fig1, ax1 = plt.subplots()
ax1.plot(range(1,11), wcss)
ax1.set_title("Elbow Method")
ax1.set_xlabel("Clusters")
ax1.set_ylabel("WCSS")

st.pyplot(fig1)

# ----------- KMEANS -----------
st.header("KMeans Clustering")

kmeans = KMeans(n_clusters=5, random_state=42)
y_kmeans = kmeans.fit_predict(x_scaled)

fig2, ax2 = plt.subplots()
ax2.scatter(x_scaled[:,0], x_scaled[:,1], c=y_kmeans)
ax2.set_title("KMeans Clustering")

st.pyplot(fig2)

# ----------- HIERARCHICAL -----------
st.header("Hierarchical Clustering")

hc = AgglomerativeClustering(n_clusters=5)
y_hc = hc.fit_predict(x_scaled)

fig3, ax3 = plt.subplots()
ax3.scatter(x_scaled[:,0], x_scaled[:,1], c=y_hc)
ax3.set_title("Hierarchical Clustering")

st.pyplot(fig3)

# ----------- DBSCAN -----------
st.header("DBSCAN Clustering")

dbscan = DBSCAN(eps=0.5, min_samples=5)
y_dbscan = dbscan.fit_predict(x_scaled)

fig4, ax4 = plt.subplots()
ax4.scatter(x_scaled[:,0], x_scaled[:,1], c=y_dbscan)
ax4.set_title("DBSCAN Clustering")

st.pyplot(fig4)

# ----------- GMM + PCA -----------
st.header("GMM Clustering")

pca = PCA(n_components=2)
x_pca = pca.fit_transform(x_scaled)

gmm = GaussianMixture(n_components=5, random_state=42)
y_gmm = gmm.fit_predict(x_pca)

fig5, ax5 = plt.subplots()
ax5.scatter(x_pca[:,0], x_pca[:,1], c=y_gmm)
ax5.set_title("GMM Clustering")

st.pyplot(fig5)

# ----------- ASSOCIATION RULES -----------
st.header("Association Rule Learning")

dataset = [
    ['milk','bread','butter','eggs'],
    ['milk','bread'],
    ['bread','eggs','butter'],
    ['bread','eggs'],
    ['bread']
]

te = TransactionEncoder()
te_array = te.fit_transform(dataset)
df = pd.DataFrame(te_array, columns=te.columns_)

# ----------- APRIORI -----------
frequent_patterns = apriori(df, min_support=0.5, use_colnames=True)
rules = association_rules(frequent_patterns, metric='confidence')

# FIX frozenset issue
rules_display = rules.copy()
rules_display['antecedents'] = rules_display['antecedents'].apply(lambda x: ', '.join(list(x)))
rules_display['consequents'] = rules_display['consequents'].apply(lambda x: ', '.join(list(x)))

st.subheader("Apriori Rules")
st.write(rules_display[['antecedents','consequents','support','confidence','lift']])

# ----------- FP-GROWTH -----------
frequent_itemsets = fpgrowth(df, min_support=0.4, use_colnames=True)

fp_display = frequent_itemsets.copy()
fp_display['itemsets'] = fp_display['itemsets'].apply(lambda x: ', '.join(list(x)))

st.subheader("FP-Growth Itemsets")
st.write(fp_display)