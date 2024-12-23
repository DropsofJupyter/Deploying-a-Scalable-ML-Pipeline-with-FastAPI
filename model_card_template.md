## MODEL CARD
## Model Details
Developer: Jesse Quinn Morrow
Model Version: 1.0.0
Model Type: Logistic Regression
- Model trained on the census.csv dataset at https://archive.ics.uci.edu/dataset/20/census+income
- Uses default sklearn.linear_model.LogisticRegression parameters, no additional input required by the user.
-sklearn docs at https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.LogisticRegression.html

## Intended Use
Model developed to predict whether salary is likely to be either '<= 50K' or '>= 50K' via an api that accepts a json object containing single values, each corresponding to a field present in the census.csv dataset that was used for training.

## Training Data

The census.csv dataset was chosen as it is likely one of the most expansive publically available datasets that includes salary.

https://archive.ics.uci.edu/dataset/20/census+income


## Evaluation Data
List of census.csv attributes:

>50K, <=50K.

age: continuous.

workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.

fnlwgt: continuous.

education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.

education-num: continuous.

marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.

occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.

relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.

race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.

sex: Female, Male.

capital-gain: continuous.

capital-loss: continuous.

hours-per-week: continuous.

native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.


## Metrics
Trained model produces the following metrics:

Precision: 0.7178
Recall: 0.2627
F1: 0.3847

## Ethical Considerations
A detailed slice analysis was performed to identify which values in each field performed poorly as predictors. The results were saved in the slice_output.txt file.

Results as follows:

workclass: ?, Count: 562
Precision: 0.6897 | Recall: 0.3509 | F1: 0.4651
workclass: Federal-gov, Count: 295
Precision: 0.7188 | Recall: 0.2072 | F1: 0.3217
workclass: Local-gov, Count: 609
Precision: 0.6613 | Recall: 0.2278 | F1: 0.3388
workclass: Never-worked, Count: 2
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
workclass: Private, Count: 6,812
Precision: 0.6715 | Recall: 0.2502 | F1: 0.3645
workclass: Self-emp-inc, Count: 316
Precision: 0.9412 | Recall: 0.3459 | F1: 0.5059
workclass: Self-emp-not-inc, Count: 757
Precision: 0.7195 | Recall: 0.2810 | F1: 0.4041
workclass: State-gov, Count: 413
Precision: 0.7561 | Recall: 0.2844 | F1: 0.4133
workclass: Without-pay, Count: 3
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
education: 10th, Count: 272
Precision: 0.5455 | Recall: 0.3000 | F1: 0.3871
education: 11th, Count: 359
Precision: 0.4286 | Recall: 0.2727 | F1: 0.3333
education: 12th, Count: 123
Precision: 0.5000 | Recall: 0.1818 | F1: 0.2667
education: 1st-4th, Count: 53
Precision: 0.3333 | Recall: 0.2500 | F1: 0.2857
education: 5th-6th, Count: 104
Precision: 0.2857 | Recall: 0.3333 | F1: 0.3077
education: 7th-8th, Count: 204
Precision: 0.4000 | Recall: 0.3636 | F1: 0.3810
education: 9th, Count: 162
Precision: 0.1667 | Recall: 0.1429 | F1: 0.1538
education: Assoc-acdm, Count: 319
Precision: 0.7273 | Recall: 0.3077 | F1: 0.4324
education: Assoc-voc, Count: 398
Precision: 0.6154 | Recall: 0.2376 | F1: 0.3429
education: Bachelors, Count: 1,637
Precision: 0.8478 | Recall: 0.2838 | F1: 0.4253
education: Doctorate, Count: 132
Precision: 0.9688 | Recall: 0.3370 | F1: 0.5000
education: HS-grad, Count: 3,110
Precision: 0.5272 | Recall: 0.2038 | F1: 0.2939
education: Masters, Count: 497
Precision: 0.8734 | Recall: 0.2644 | F1: 0.4059
education: Preschool, Count: 18
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
education: Prof-school, Count: 179
Precision: 0.9630 | Recall: 0.3824 | F1: 0.5474
education: Some-college, Count: 2,202
Precision: 0.5926 | Recall: 0.2248 | F1: 0.3260
marital-status: Divorced, Count: 1,348
Precision: 0.5385 | Recall: 0.3203 | F1: 0.4016
marital-status: Married-AF-spouse, Count: 10
Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
marital-status: Married-civ-spouse, Count: 4,454
Precision: 0.8294 | Recall: 0.2456 | F1: 0.3789
marital-status: Married-spouse-absent, Count: 124
Precision: 0.5000 | Recall: 0.3333 | F1: 0.4000
marital-status: Never-married, Count: 3,209
Precision: 0.3581 | Recall: 0.3510 | F1: 0.3545
marital-status: Separated, Count: 302
Precision: 0.4706 | Recall: 0.4444 | F1: 0.4571
marital-status: Widowed, Count: 322
Precision: 0.5455 | Recall: 0.4286 | F1: 0.4800
occupation: ?, Count: 564
Precision: 0.6897 | Recall: 0.3509 | F1: 0.4651
occupation: Adm-clerical, Count: 1,154
Precision: 0.4533 | Recall: 0.2138 | F1: 0.2906
occupation: Armed-Forces, Count: 1
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
occupation: Craft-repair, Count: 1,232
Precision: 0.5600 | Recall: 0.2029 | F1: 0.2979
occupation: Exec-managerial, Count: 1,219
Precision: 0.8643 | Recall: 0.2976 | F1: 0.4427
occupation: Farming-fishing, Count: 287
Precision: 0.5263 | Recall: 0.2778 | F1: 0.3636
occupation: Handlers-cleaners, Count: 423
Precision: 0.5000 | Recall: 0.3030 | F1: 0.3774
occupation: Machine-op-inspct, Count: 602
Precision: 0.4444 | Recall: 0.2462 | F1: 0.3168
occupation: Other-service, Count: 1,000
Precision: 0.2121 | Recall: 0.1707 | F1: 0.1892
occupation: Priv-house-serv, Count: 42
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
occupation: Prof-specialty, Count: 1,261
Precision: 0.8750 | Recall: 0.2917 | F1: 0.4375
occupation: Protective-serv, Count: 184
Precision: 0.6667 | Recall: 0.1667 | F1: 0.2667
occupation: Sales, Count: 1,038
Precision: 0.7451 | Recall: 0.2815 | F1: 0.4086
occupation: Tech-support, Count: 285
Precision: 0.8947 | Recall: 0.1848 | F1: 0.3063
occupation: Transport-moving, Count: 477
Precision: 0.4828 | Recall: 0.1458 | F1: 0.2240
relationship: Husband, Count: 3,917
Precision: 0.8304 | Recall: 0.2447 | F1: 0.3780
relationship: Not-in-family, Count: 2,547
Precision: 0.4794 | Recall: 0.3419 | F1: 0.3991
relationship: Other-relative, Count: 292
Precision: 0.3333 | Recall: 0.4286 | F1: 0.3750
relationship: Own-child, Count: 1,510
Precision: 0.1905 | Recall: 0.3810 | F1: 0.2540
relationship: Unmarried, Count: 1,034
Precision: 0.5238 | Recall: 0.3333 | F1: 0.4074
relationship: Wife, Count: 469
Precision: 0.8529 | Recall: 0.2500 | F1: 0.3867
race: Amer-Indian-Eskimo, Count: 95
Precision: 0.5714 | Recall: 0.3333 | F1: 0.4211
race: Asian-Pac-Islander, Count: 307
Precision: 0.6774 | Recall: 0.2593 | F1: 0.3750
race: Black, Count: 949
Precision: 0.5918 | Recall: 0.2636 | F1: 0.3648
race: Other, Count: 72
Precision: 0.0000 | Recall: 0.0000 | F1: 0.0000
race: White, Count: 8,346
Precision: 0.7156 | Recall: 0.2609 | F1: 0.3824
sex: Female, Count: 3,264
Precision: 0.5692 | Recall: 0.3000 | F1: 0.3929
sex: Male, Count: 6,505
Precision: 0.7415 | Recall: 0.2534 | F1: 0.3777
native-country: ?, Count: 169
Precision: 0.9375 | Recall: 0.3750 | F1: 0.5357
native-country: Cambodia, Count: 6
Precision: 1.0000 | Recall: 0.5000 | F1: 0.6667
native-country: Canada, Count: 39
Precision: 0.6667 | Recall: 0.2222 | F1: 0.3333
native-country: China, Count: 25
Precision: 0.5000 | Recall: 0.2000 | F1: 0.2857
native-country: Columbia, Count: 19
Precision: 0.0000 | Recall: 0.0000 | F1: 0.0000
native-country: Cuba, Count: 25
Precision: 1.0000 | Recall: 0.1667 | F1: 0.2857
native-country: Dominican-Republic, Count: 22
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Ecuador, Count: 7
Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
native-country: El-Salvador, Count: 36
Precision: 0.0000 | Recall: 0.0000 | F1: 0.0000
native-country: England, Count: 23
Precision: 0.5000 | Recall: 0.1429 | F1: 0.2222
native-country: France, Count: 9
Precision: 1.0000 | Recall: 0.2500 | F1: 0.4000
native-country: Germany, Count: 39
Precision: 1.0000 | Recall: 0.2667 | F1: 0.4211
native-country: Greece, Count: 13
Precision: 0.6667 | Recall: 0.5000 | F1: 0.5714
native-country: Guatemala, Count: 17
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Haiti, Count: 15
Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
native-country: Holand-Netherlands, Count: 1
Precision: 0.0000 | Recall: 1.0000 | F1: 0.0000
native-country: Honduras, Count: 6
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Hong, Count: 4
Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
native-country: Hungary, Count: 3
Precision: 0.0000 | Recall: 0.0000 | F1: 0.0000
native-country: India, Count: 30
Precision: 1.0000 | Recall: 0.3333 | F1: 0.5000
native-country: Iran, Count: 16
Precision: 1.0000 | Recall: 0.1429 | F1: 0.2500
native-country: Ireland, Count: 9
Precision: 1.0000 | Recall: 0.5000 | F1: 0.6667
native-country: Italy, Count: 26
Precision: 1.0000 | Recall: 0.4286 | F1: 0.6000
native-country: Jamaica, Count: 21
Precision: 1.0000 | Recall: 0.5000 | F1: 0.6667
native-country: Japan, Count: 19
Precision: 1.0000 | Recall: 0.3333 | F1: 0.5000
native-country: Laos, Count: 6
Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
native-country: Mexico, Count: 180
Precision: 0.6000 | Recall: 0.2500 | F1: 0.3529
native-country: Nicaragua, Count: 14
Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
native-country: Outlying-US(Guam-USVI-etc), Count: 5
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Peru, Count: 14
Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
native-country: Philippines, Count: 56
Precision: 0.6667 | Recall: 0.2222 | F1: 0.3333
native-country: Poland, Count: 14
Precision: 0.5000 | Recall: 0.2500 | F1: 0.3333
native-country: Portugal, Count: 13
Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
native-country: Puerto-Rico, Count: 37
Precision: 0.0000 | Recall: 0.0000 | F1: 0.0000
native-country: Scotland, Count: 6
Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
native-country: South, Count: 24
Precision: 0.3333 | Recall: 0.2500 | F1: 0.2857
native-country: Taiwan, Count: 16
Precision: 0.6667 | Recall: 0.2857 | F1: 0.4000
native-country: Thailand, Count: 6
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: Trinadad&Tobago, Count: 7
Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
native-country: United-States, Count: 8,746
Precision: 0.7003 | Recall: 0.2598 | F1: 0.3790
native-country: Vietnam, Count: 19
Precision: 0.3333 | Recall: 0.3333 | F1: 0.3333
native-country: Yugoslavia, Count: 7
Precision: 1.0000 | Recall: 0.2500 | F1: 0.4000


## Caveats and Recommendations
This model is not built to predict specific values, but rather to predict only whether someone makes more or less than 50 thousand dollars.

Example of dataset values for input at inference are as follows:

data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

