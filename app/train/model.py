"""
Specify the structure of a trained XGB model
"""

from dataclasses import dataclass
from xgboost import XGBClassifier

@dataclass
class XGBModel:
    """
    XGBClassifier model, an implementation of gradient boosted 
    decision trees designed for speed and performance.

    Param:
        -
        -
    """

    _model: XGBClassifier

    @classmethod
    def new_model(cls: type[XGBClassifier],
                  max_depth: int,
                  learning_rate: float,
                  n_estimators: int,
                  objective: str,
                  booster: str,
                  n_jobs: int,
                  gamma: float,
                  subsample: float,
                  colsample_bytree: int,
                  colsample_bylevel: int,
                  colsample_bynode: int,
                  reg_alpha: int,
                  reg_lambda: int,
                  scale_pos_weight: int,
                  base_score: float,
                  random_state: int,
                  missing: int,
                  use_label_encoder: bool = False) -> XGBClassifier:
        """

        Returns
        -------
        object
        """
        instance = cls(_model=None)

        instance._model = XGBClassifier(max_depth=max_depth,
                                        learning_rate=learning_rate,
                                        n_estimators=n_estimators,
                                        verbosity=1,
                                        objective=objective,
                                        booster=booster,
                                        n_jobs=n_jobs,
                                        gamma=gamma,
                                        subsample=subsample,
                                        colsample_bytree=colsample_bytree,
                                        colsample_bylevel=colsample_bylevel,
                                        colsample_bynode=colsample_bynode,
                                        reg_alpha=reg_alpha,
                                        reg_lambda=reg_lambda,
                                        scale_pos_weight=scale_pos_weight,
                                        base_score=base_score,
                                        random_state=random_state,
                                        missing=missing,
                                        use_label_encoder=use_label_encoder
                                        )

        return instance._model
