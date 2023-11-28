## Feedback

Verbal delivery: 18/20 
Slides: 18/20
Data pipeline: 18/20
Modeling process: 20/20
Repo: 19/20

TOTAL: 93/100

Comments:
Good job!
You correctly realized that there are several groups of features, good job using sequence matcher and reducing your feature set.  Good comparision of the models you considered, but how are the metrics calculated - using CV or a val set?  Embedded methods e.g. RF feature importance could be run with the 400+ features you had after doing the filtering, as other teams did, to get a final feature set - this might lead to a more robust feature set than univariate methods alone.  How are you calculating MAPE - at an aggregated storm level or per grid cell, and how did you deal with the 0 values in calculating MAPE.  Some functions/methods in repo are missing docstrings.  More analysis/interpretation of your results would have been good - e.g. for which locations did the model work well/not work well?  For which types of storms?  Were there particular events it did very poorly on?