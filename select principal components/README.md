# Selecting the number of Principal Components

The first time I was tasked with finding the principal components, I found myself manually adding the numbers thrown at me as the output of the code I'd just written. All we were told was that as a rule of thumb try to get as many variables that could explain at least 80% of the variability. 

The next time I applied PCA, the dataset had close to 200 variables and to keep adding until I hit 80% seemed like too much. That is when I researched online and found a nifty solution: To plot it!

Just four additional lines of code gives you a nice graph that helps you make that split second decision. The graph is _cumulative explained variance_ vs _number of components_. I used the wines dataset to show this.

From the graph below we can see that __2__ components alone explains almost __92%__ of the variability in the dataset.

<p align="center">
  <img title='Number of Principal Components' src='https://github.com/anxrxdh/data-science-minis/blob/master/select%20principal%20components/plots/no%20of%20princomps.JPG'>
</p>

