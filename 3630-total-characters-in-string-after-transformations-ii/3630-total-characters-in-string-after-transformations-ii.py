def matrix_multiply(A, B, MOD):
    """Multiply two matrices and take modulo of each element."""
    n = len(A)
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
    
    return result

def matrix_power(A, power, MOD):
    """Compute A^power using binary exponentiation."""
    n = len(A)
    result = [[0] * n for _ in range(n)]   
    for i in range(n):
        result[i][i] = 1
    
    while power > 0:
        if power % 2 == 1:
            result = matrix_multiply(result, A, MOD)
        A = matrix_multiply(A, A, MOD)
        power //= 2
    
    return result

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        char_count = [0] * 26
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        
        transformation_matrix = [[0] * 26 for _ in range(26)]
        
        for i in range(26):  
            count = nums[i]  
            current = i
            for _ in range(count):
                current = (current + 1) % 26  
                transformation_matrix[i][current] += 1
        
        result_matrix = matrix_power(transformation_matrix, t, MOD)
        
        total_length = 0
        for i in range(26): 
            for j in range(26): 
                total_length = (total_length + char_count[i] * result_matrix[i][j]) % MOD
        
        return total_length