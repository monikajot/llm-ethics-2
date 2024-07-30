from functions import query_model


# generate 50 examples of positive sensitivity
# generate 50 examples of negative sensitivity

message = ""
system = ""
query_model("gpt-3.5", message, system)
