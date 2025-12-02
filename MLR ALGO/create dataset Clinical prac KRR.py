import pandas as pd

df = pd.DataFrame({

    'DISEASE_CARDIOVASCULAR':['heart_association_class:','class1 no_limit' , 'class2 slight limit' , 'class3 Marked limit No symptoms  at rest' , 'class4 Marked limit No symptoms  at rest'],
    
    'CHEST_PAIN':['Cardiac' , 'pressure','tightness' , 'physical stress' , 'prolonged symtoms'],
    
    'NON_CARDIAC':['sharp' , 'stubbing' , 'focal' , 'well localized' , 'at rest'],
    
    'DIAGNOSTIC TESTS':['Cardiac catheterization' , 'ECG/EKG' , 'Echocardiogram' , 'Chest X-rays' , 'Blood test'],
    
    '1st LINE TREATMENT':['Supplement O2' , 'Control chest pain by(pain killer)' , 'Provide fluid support' , 'Medications 4th to remove excess fluid' , 'Administration'],
    
    'HEART_DISEASE(SYMPTOMS)':['H.R' , 'Breathing' , 'sweat' , 'cyanosis' , 'tiredness'],
    
    "age": [63, 37, 41, 56, 57],
    
    "sex": [1, 1, 0, 1, 0],
    
    'ECG' : 'Most common diagnosis for (VSD)',
    
    "target": [1, 1, 0, 1, 1],
    
    "chol": [233, 250, 204, 236, 354],

})
print(df)
print(df.shape)# (5, 11)
print(df.columns)
# Index(['DISEASE_CARDIOVASCULAR', 'CHEST_PAIN', 'NON_CARDIAC',
#        'DIAGNOSTIC TESTS', '1st LINE TREATMENT', 'HEART_DISEASE(SYMPTOMS)',
#        'age', 'sex', 'ECG', 'target', 'chol'],
#       dtype='object')


