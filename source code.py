import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import ipywidgets as widgets
from IPython.display import display, clear_output, HTML

data = pd.read_csv("/content/disease_data.csv")

X = data.drop("disease", axis=1)
response = data["disease"]

model = RandomForestClassifier(random_state=42)
model.fit(X, response)

symptoms = list(X.columns)

symptom_checkboxes = {}
checkbox_widgets = []

for symptom in symptoms:
    cb = widgets.Checkbox(
        value=False,
        description=symptom.replace("_", " ").title(),
        layout=widgets.Layout(width="220px")
    )
    symptom_checkboxes[symptom] = cb
    checkbox_widgets.append(cb)

grid = widgets.GridBox(
    checkbox_widgets,
    layout=widgets.Layout(grid_template_columns="repeat(2, 250px)")
)

predict_button = widgets.Button(
    description="Predict Disease",
    button_style='',
    layout=widgets.Layout(width="220px", height="45px")
)

output_area = widgets.Output()

# Inject dark theme CSS (corrected from previous cell)
display(HTML("""
<style>
body {
    background-color: #0f172a;
}

.widget-label {
    color: #e2e8f0 !important;
    font-size: 14px;
}

div.widget-checkbox {
    margin: 5px;
}

button {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white !important;
    border-radius: 10px !important;
    border: none !important;
    font-weight: bold;
}

button:hover {
    transform: scale(1.05);
    transition: 0.2s;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
"""))


def predict_disease_ipywidgets(b):
    with output_area:
        clear_output()

        input_data = [[1 if symptom_checkboxes[s].value else 0 for s in symptoms]]

        prediction = model.predict(input_data)
        probabilities = model.predict_proba(input_data)

        predicted_class_index = list(model.classes_).index(prediction[0])
        confidence = probabilities[0][predicted_class_index] * 100

        # Corrected HTML display (fixed f-string syntax)
        display(HTML(f"""
        <div style="
            animation: fadeIn 0.8s;
            padding: 20px;
            border-radius: 12px;
            background: #1e293b;
            border: 1px solid #334155;
            color: #e2e8f0;
            width: fit-content;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
        ">
            <h3 style="color:#a78bfa;">Prediction Result</h3>
            <p><b>Disease:</b> {prediction[0]}</p>
            <p><b>Confidence:</b> {confidence:.2f}%</p>
        </div>
        """))

predict_button.on_click(predict_disease_ipywidgets)

# Title + subtitle (corrected indentation and content)
title = widgets.HTML("""
<h2 style='color:#e2e8f0;'>Disease Prediction System</h2>
""")

subtitle = widgets.HTML("""
<p style='color:#94a3b8;'>Select your symptoms and click predict</p>
""")

# Layout (corrected indentation)
ui = widgets.VBox([
    title,
    subtitle,
    grid,
    widgets.HBox([predict_button]),
    output_area
])

display(ui)
