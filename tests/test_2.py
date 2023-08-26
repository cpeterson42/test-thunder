import tensorflow as tf

def test_function():
    # Check if GPU is available
    if not tf.config.list_physical_devices('GPU'):
        return "No GPU available"
    
    # Create two random matrices of different sizes
    matrix1 = tf.random.uniform((2000, 1500))
    matrix2 = tf.random.uniform((1500, 1700))
    
    # Perform matrix multiplication on GPU
    product = tf.matmul(matrix1, matrix2)
    
    # Average of the resulting matrix (for demonstration purposes)
    average_result = tf.reduce_mean(product).numpy()
    
    return average_result
