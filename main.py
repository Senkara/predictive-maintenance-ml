import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


def load_dataset():
    """
    Dataset is expected to be inside the data folder.
    """

    data_path = Path("data") / "predictive_maintenance.csv"

    if not data_path.exists():
        data_path = Path("predictive_maintenance.csv")

    if not data_path.exists():
        raise FileNotFoundError(
            "Dataset not found. Please place predictive_maintenance.csv "
            "inside the data folder."
        )

    df = pd.read_csv(data_path)

    print("\n===== Dataset Loaded =====")
    print(df.head())
    print("\nDataset Shape:", df.shape)

    return df


def preprocess_data(df):
    """
    Prepares the dataset for machine learning.
    """

    print("\n===== Missing Values =====")
    print(df.isnull().sum())

    df = df.dropna()

    df["Type"] = df["Type"].map({
        "L": 0,
        "M": 1,
        "H": 2
    })

    columns_to_drop = [
        "UDI",
        "Product ID",
        "Failure Type"
    ]

    df_model = df.drop(
        columns=columns_to_drop
    )

    X = df_model.drop("Target", axis=1)
    y = df_model["Target"]

    print("\n===== Target Distribution =====")
    print(y.value_counts())

    return X, y


def evaluate_model(model_name, model, X_test, y_test):
    """
    Evaluates a trained model and returns performance metrics.
    """

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    precision = precision_score(
        y_test,
        predictions,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        predictions,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        predictions,
        zero_division=0
    )

    print(f"\n===== {model_name} =====")
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1)

    print("\nConfusion Matrix:")
    print(confusion_matrix(
        y_test,
        predictions
    ))

    print("\nClassification Report:")
    print(classification_report(
        y_test,
        predictions,
        zero_division=0
    ))

    return {
        "Model": model_name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    }


def plot_feature_importance(model, X):
    """
    Shows feature importance for Random Forest model.
    """

    feature_importance = pd.DataFrame({
        "Feature": X.columns,
        "Importance": model.feature_importances_
    })

    feature_importance = feature_importance.sort_values(
        by="Importance",
        ascending=False
    )

    print("\n===== Feature Importance - Random Forest =====")
    print(feature_importance)

    plt.figure(figsize=(8, 5))
    plt.barh(
        feature_importance["Feature"],
        feature_importance["Importance"]
    )
    plt.xlabel("Importance")
    plt.ylabel("Feature")
    plt.title("Feature Importance - Random Forest")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()


def main():
    df = load_dataset()

    X, y = preprocess_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    models = {
        "Logistic Regression": Pipeline([
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(
                max_iter=1000,
                random_state=42
            ))
        ]),

        "Decision Tree": DecisionTreeClassifier(
            random_state=42
        ),

        "Random Forest": RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ),

        "Balanced Random Forest": RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            class_weight="balanced"
        ),

        "Gradient Boosting": GradientBoostingClassifier(
            random_state=42
        )
    }

    results = []
    trained_models = {}

    for model_name, model in models.items():
        model.fit(
            X_train,
            y_train
        )

        trained_models[model_name] = model

        result = evaluate_model(
            model_name,
            model,
            X_test,
            y_test
        )

        results.append(result)

    comparison = pd.DataFrame(results)

    comparison = comparison.sort_values(
        by="F1 Score",
        ascending=False
    )

    print("\n===== Model Comparison =====")
    print(comparison)

    best_model = comparison.iloc[0]

    print("\n===== Best Model =====")
    print("Best Model:", best_model["Model"])
    print("Accuracy:", best_model["Accuracy"])
    print("Precision:", best_model["Precision"])
    print("Recall:", best_model["Recall"])
    print("F1 Score:", best_model["F1 Score"])

    random_forest_model = trained_models["Random Forest"]

    plot_feature_importance(
        random_forest_model,
        X
    )


if __name__ == "__main__":
    main()