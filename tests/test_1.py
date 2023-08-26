import tensorflow as tf

def test_function():
    # Check if GPU is available
    if not tf.config.list_physical_devices('GPU'):
        return "No GPU available"
    
    # Create two random matrices
    matrix1 = tf.random.uniform((1000, 1000))
    matrix2 = tf.random.uniform((1000, 1000))
    
    # Perform matrix multiplication on GPU
    product = tf.matmul(matrix1, matrix2)
    
    # Sum of the resulting matrix (for demonstration purposes)
    sum_result = tf.reduce_sum(product).numpy()
    
    return sum_result
