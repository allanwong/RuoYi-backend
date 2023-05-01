# -*- coding: utf-8 -*-
"""
@Author  : gpf
@License : (C) Copyright 2023
@Time    : 2023/04/18 13:06

"""
# %% 导入相关包
import numpy as np
import pandas as pd
import json
# import sklearn.tree as st
# import sklearn.feature_selection as sf
# import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn.tree import plot_tree, DecisionTreeClassifier  # 树图
# from sklearn import datasets
# from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier

def importData(data):
    Fault_diagnosis_data = pd.read_csv(data,
                                       usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                                20,
                                                21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                                                39,
                                                40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
                                                58,
                                                59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76,
                                                77,
                                                78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95,
                                                96,
                                                97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108])
    return Fault_diagnosis_data

def data_process(Fault_diagnosis_data,feature_mean,feature_median,feature_mode):
    length1 = len(feature_mean)
    i = 0
    while i < length1:
        Fault_diagnosis_data[feature_mean[i]].fillna(Fault_diagnosis_data[feature_mean[i]].mean(),
                                                     inplace=True)  # 使用该列平均值进行空缺值替换
        i += 1

    length2 = len(feature_median)
    j = 0
    while j < length2:
        Fault_diagnosis_data[feature_median[j]].fillna(Fault_diagnosis_data[feature_median[j]].median(), inplace=True)
        j += 1

    length3 = len(feature_mode)
    k = 0
    while k < length3:
        Fault_diagnosis_data[feature_mode[k]].fillna(Fault_diagnosis_data[feature_mode[k]].mode().iloc[0], inplace=True)
        k += 1

def loadData(Fault_diagnosis_data):
    # 载入特征和标签集
    X_test = Fault_diagnosis_data[
        ['feature0', 'feature1', 'feature2', 'feature3', 'feature4', 'feature5', 'feature6', 'feature7', 'feature8',
         'feature9', 'feature10', 'feature11', 'feature12', 'feature13', 'feature14', 'feature15', 'feature16',
         'feature17',
         'feature18', 'feature19', 'feature20', 'feature21', 'feature22', 'feature23', 'feature24', 'feature25',
         'feature26', 'feature27', 'feature28', 'feature29', 'feature30', 'feature31', 'feature32', 'feature33',
         'feature34', 'feature35', 'feature36', 'feature37', 'feature38', 'feature39', 'feature40', 'feature41',
         'feature42', 'feature43', 'feature44', 'feature45', 'feature46', 'feature47', 'feature48', 'feature49',
         'feature50', 'feature51', 'feature52', 'feature53', 'feature54', 'feature55', 'feature56', 'feature57',
         'feature58', 'feature59', 'feature60', 'feature61', 'feature62', 'feature63', 'feature64', 'feature65',
         'feature66', 'feature67', 'feature68', 'feature69', 'feature70', 'feature71', 'feature72', 'feature73',
         'feature74', 'feature75', 'feature76', 'feature77', 'feature78', 'feature79', 'feature80', 'feature81',
         'feature82', 'feature83', 'feature84', 'feature85', 'feature86', 'feature87', 'feature88', 'feature89',
         'feature90', 'feature91', 'feature92', 'feature93', 'feature94', 'feature95', 'feature96', 'feature97',
         'feature98', 'feature99', 'feature100', 'feature101', 'feature102', 'feature103', 'feature104', 'feature105',
         'feature106']]
    y_test = Fault_diagnosis_data['label']
    
    return X_test,y_test



def classify(filepath):
    data_test = filepath
    data_train = "D:SoftCup\preprocess_train.csv"

    #数据读取
    Fault_diagnosis_data_train = importData(data_train)
    Fault_diagnosis_data_test = importData(data_test)

    feature_mean = ['feature0', 'feature2', 'feature4', 'feature7', 'feature8', 'feature11', 'feature15', 'feature22',
                    'feature23',
                    'feature27', 'feature28', 'feature30', 'feature38', 'feature41', 'feature42', 'feature43',
                    'feature48',
                    'feature49',
                    'feature51', 'feature56', 'feature58', 'feature63', 'feature70', 'feature71', 'feature75',
                    'feature79',
                    'feature81',
                    'feature82', 'feature84', 'feature85', 'feature86', 'feature95', 'feature96', 'feature99',
                    'feature102',
                    'feature106']
    feature_median = ['feature3', 'feature10', 'feature12', 'feature17', 'feature18', 'feature21', 'feature24',
                      'feature25',
                      'feature26',
                      'feature29', 'feature34', 'feature37', 'feature40', 'feature45', 'feature47', 'feature50',
                      'feature52', 'feature53',
                      'feature55', 'feature62', 'feature68', 'feature69', 'feature73', 'feature74', 'feature83',
                      'feature90', 'feature93',
                      'feature98', 'feature103', 'feature104']
    feature_mode = ['feature1', 'feature20', 'feature32', 'feature54', 'feature60', 'feature64', 'feature65',
                    'feature78',
                    'feature80',
                    'feature88', 'feature92']
    
    # 数据处理
    data_process(Fault_diagnosis_data_train,feature_mean,feature_median,feature_mode)
    data_process(Fault_diagnosis_data_test,feature_mean,feature_median,feature_mode)

    # 载入特征和标签集
    X_train,y_train = loadData(Fault_diagnosis_data_train)
    X_test,y_test = loadData(Fault_diagnosis_data_test)


    #取训练集
    X_rf_train = X_train
    y_rf_train = y_train
    #    X_rf_train = X_test

    # 取测试集
    X_rf_test = X_test
    y_rf_test = y_test

    # 建立随机森林模型
    rfc = RandomForestClassifier(n_estimators=281, criterion='gini', max_depth=18, max_features=107, random_state=100)
    rfc.fit(X_rf_train, y_rf_train)  # 模型训练
    y_rf_pred = rfc.predict(X_rf_test)  # 使用随机森林（281个决策树分类器）多数投票产生的预测label列表(测试集改为1000条样本)

    # length_train = len(X_test)
    length_test = len(y_rf_test)  # 500

    TP = 0
    FP = 0
    TN = 0
    FN = 0
    item = 0

    a = 0
    # 创建列表存放每一个类别的预测准确率和召回率
    # accuracy_i = []
    precision_i = []
    recall_i = []
    # 循环向列表中写入数据
    while a < 6:
        while item < length_test:  # 500
            if a == y_rf_pred[item]:
                if a == y_rf_test.values[item]:
                    TP += 1
                else:
                    FP += 1
            else:
                if a == y_rf_test.values[item]:
                    FN += 1
                else:
                    TN += 1
            item += 1
        print("Label为%d的指标：TP:%d,TN:%d,FP:%d,FN:%d" % (a, TP, TN, FP, FN))
        # macro_accuracy.append((TP + TN) / (TP + TN + FP + FN))    # 准确率
        precision_i.append(TP / (TP + FP))  # 精确率
        recall_i.append(TP / (TP + FN))  # 召回率
        print("precision_i:", precision_i)
        print("recall_i:", recall_i)
        a += 1
        TP, FP, TN, FN, item = 0, 0, 0, 0, 0

    b = 0
    jtem = 0
    LabelSum_i = [0, 0, 0, 0, 0, 0]

    LABEL0 = 0
    LABEL1 = 0
    LABEL2 = 0
    LABEL3 = 0
    LABEL4 = 0
    LABEL5 = 0

    while jtem < length_test:
        if 0 == y_rf_test.values[jtem]:
            LABEL0 += 1
        elif 1 == y_rf_test.values[jtem]:
            LABEL1 += 1
        elif 2 == y_rf_test.values[jtem]:
            LABEL2 += 1
        elif 3 == y_rf_test.values[jtem]:
            LABEL3 += 1
        elif 4 == y_rf_test.values[jtem]:
            LABEL4 += 1
        else:
            LABEL5 += 1
        jtem += 1
    # print(LabelSum_i[b])  # 测试集中每一类的样本数量
    # b += 1

    # %%
    # 模型评价指标
    sum = 0
    sun = 0
    for p in precision_i:
        sum += p
    macro_P = sum / len(precision_i)
    print("macro_P:", macro_P)

    for r in recall_i:
        sun += r
    macro_R = sun / len(recall_i)
    print("macro_R:", macro_R)
    macro_F1 = (2 * macro_P * macro_R) / (macro_P + macro_R)
    print("macro_F1:", macro_F1)
    print("排行得分：", 100 * (2 * macro_P * macro_R) / (macro_P + macro_R))

    # %%模型评估
    print("Test set predictions: \n {}".format(y_rf_pred))
    print("Test_Set Score: {:.15f}".format(np.mean(y_rf_pred == y_rf_test)))  # np.mean函数输出两个矩阵/数组的相似程度

    # %%
    # LABEL0 = LabelSum_i[0]
    # LABEL1 = LabelSum_i[1]
    # LABEL2 = LabelSum_i[2]
    # LABEL3 = LabelSum_i[3]
    # LABEL4 = LabelSum_i[4]
    # LABEL5 = LabelSum_i[5]

    # 测试结果json文件输出
    dictionary = {}
    keys = []
    values = []
    for i in range(len(y_rf_test)):
        keys.append((str(y_rf_test.index[i])))
        values.append(int(y_rf_pred[i]))
    print(keys)
    print(values)

    for key, value in zip(keys, values):
        dictionary[key] = value
    print(dictionary)

    # with open('./data/classifyResults.json', 'w') as json_file:
    with open('./media/data/classifyResults.json', 'w') as json_file:
        json.dump(dictionary, json_file, indent=4)

    return macro_P, macro_R, macro_F1, LABEL0, LABEL1, LABEL2, LABEL3, LABEL4, LABEL5, precision_i, recall_i
