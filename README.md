# AcademicPaperRanking
An effort to analyze and rank Academic papers better than traditional h-index ranking. We will comeup with a new model by  employing numerous important features to research paper ranking rather than just the citation.

TODOs
 - Data cleaning : Big one, Data is far from ideal.
 - Homogenize data by combining DBLP and ACM data into 1 dataframe (currently only ACM version 9 is used). 
 - Define what model we need to use.
   - Include Journal ranking from Scopous as a feature: Not all journals are included in Scopus dataset.
   - Should we compare from baseline model. Lower RMSE doesn't necessarily means that we are close to best Ranking.
 - Analyze how good is PageRank as a baseline model.
 - Can we use Unsupervised learning here? If yes, HOW??? (Million dollar question)
 - Create top 100 Rank papers. 
 - Task 2 Citation Network graph.

We are just sharing common jupyter notebook here.
To view the complete project with data go to the kaggle kernal at https://www.kaggle.com/divvyam/dsf-project.

Kernel for working on MAG data: https://www.kaggle.com/gkaur1/mag-kernel
