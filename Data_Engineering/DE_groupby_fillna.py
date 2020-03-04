#How to group data and fill in nan?
#You can do this with these methods: groupby(), transform(), a lambda function, fillna(), and mean()

df.groupby(['Country Name'])['GDP'].transform(lambda x: x.fillna(x.mean()))
