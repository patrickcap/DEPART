from dataclasses import dataclass

from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier


@dataclass
class XGBModel:
    """
    XGBClassifier model, an implementation of gradient boosted decision trees designed for speed and performance.

    Param:
        -
        -
    """

    _model: XGBClassifier

    @classmethod
    def new_model(cls: type[XGBClassifier], max_depth: int, learning_rate: float, n_estimators: int, objective: str,
                  booster: str, n_jobs: int, gamma: float, subsample: float, colsample_bytree: int,
                  colsample_bylevel: int, colsample_bynode: int, reg_alpha: int, reg_lambda: int, scale_pos_weight: int,
                  base_score: float, random_state: int, missing: int, use_label_encoder: bool = False) -> XGBClassifier:
        """

        Returns
        -------
        object
        """
        instance = cls(_model=None)

        instance._model = XGBClassifier(max_depth=3,
                                        learning_rate=0.1,
                                        n_estimators=5,
                                        verbosity=1,
                                        objective='binary:logistic',
                                        booster='gbtree',
                                        n_jobs=2,
                                        gamma=0.001,
                                        subsample=0.632,
                                        colsample_bytree=1,
                                        colsample_bylevel=1,
                                        colsample_bynode=1,
                                        reg_alpha=1,
                                        reg_lambda=0,
                                        scale_pos_weight=1,
                                        base_score=0.5,
                                        random_state=20212004,
                                        missing=1,
                                        use_label_encoder=False
                                        )

        return instance._model
