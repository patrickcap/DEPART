from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier

# Create the parameter search grid
param_grid = dict({'n_estimators': [50, 200],
                   'max_depth': [3, 5, 10],
                   'learning_rate' : [0.01, 0.1],
                   'reg_alpha': [1,0]
                  })

# Define the XGB model
XGB = XGBClassifier(max_depth=3,                    # Depth of each tree
                            learning_rate=0.1,            # How much to shrink error in each subsequent training. Trade-off with no. estimators.
                            n_estimators=5,             # How many trees to use, the more the better, but decrease learning rate if many used.
                            verbosity=1,                  # If to show more errors or not.
                            objective='binary:logistic',  # Type of target variable.
                            booster='gbtree',             # What to boost. Trees in this case.
                            n_jobs=2,                     # Parallel jobs to run. Set your processor number.
                            gamma=0.001,                  # Minimum loss reduction required to make a further partition on a leaf node of the tree. (Controls growth!)
                            subsample=0.632,              # Subsample ratio. Can set lower
                            colsample_bytree=1,           # Subsample ratio of columns when constructing each tree.
                            colsample_bylevel=1,          # Subsample ratio of columns when constructing each level. 0.33 is similar to random forest.
                            colsample_bynode=1,           # Subsample ratio of columns when constructing each split.
                            reg_alpha=1,                  # Regularizer for first fit. alpha = 1, lambda = 0 is LASSO.
                            reg_lambda=0,                 # Regularizer for first fit.
                            scale_pos_weight=1,           # Balancing of positive and negative weights.
                            base_score=0.5,               # Global bias. Set to average of the target rate.
                            random_state=20212004,        # Seed
                            missing=1,                 # How are nulls encoded?
                            use_label_encoder=False       # Eliminates warning

                    )

# Define grid search object.
GridXGB = GridSearchCV(XGB,             # Original XGB.
                       param_grid,          # Parameter grid
                       cv = 5,              # Number of cross-validation folds.
                       scoring = 'balanced_accuracy', # How to rank outputs.
                       n_jobs = 2,         # Parallel jobs. -1 is "all you have"
                       refit = True,       # If refit at the end with the best. We'll do it manually.
                       verbose = 1
                      )
