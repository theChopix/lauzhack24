import pandas as pd
    
def evaluate_datasets(train, test):

    def create_pairwise_matrix(external_parties_df):
        """creates matrix that tells us if two parties are the same identity"""
        external_ids = external_parties_df['external_id'].values
        matrix = (external_ids[:, None] == external_ids).tolist()
        return matrix
    
    def compute_recall(matrix_truth, matrix_pred):
        n = len(matrix_truth)
        true_positive = 0
        false_negative = 0
        for i in range(n):
            for j in range(i + 1, n):
                if matrix_truth[i][j] and matrix_pred[i][j]:
                    true_positive += 1
                elif matrix_truth[i][j] and not matrix_pred[i][j]:
                    false_negative += 1
        recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0
        return recall

    def compute_precision(matrix_truth, matrix_pred):
        n = len(matrix_truth)
        true_positive = 0
        false_positive = 0
        for i in range(n):
            for j in range(i + 1, n):
                if matrix_truth[i][j] and matrix_pred[i][j]:
                    true_positive += 1
                elif not matrix_truth[i][j] and matrix_pred[i][j]:
                    false_positive += 1
        precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0
        return precision


    train_matrix = create_pairwise_matrix(train)
    test_matrix  = create_pairwise_matrix(test)

    recall = compute_recall(train_matrix, test_matrix)
    precision = compute_precision(train_matrix, test_matrix)

    f1 = 2 * recall * precision / (recall + precision) if (recall + precision) > 0 else 0
    return f1