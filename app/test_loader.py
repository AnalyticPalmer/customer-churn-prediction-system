from model_loader import load_model

model, preprocessor = load_model()

print(type(model))
print(type(preprocessor))