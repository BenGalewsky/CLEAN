from CLEAN.infer import infer_maxsep
train_data = "split100"
test_data = "price"
x = infer_maxsep(train_data, test_data, report_metrics=False, pretrained=True)
print("----- Result ----")
print(x)

