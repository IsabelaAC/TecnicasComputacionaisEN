#Método sobre relaxações sucessivas

import numpy as np
import ray_tracing_cuda_float as rt
import pyraft_noc as pr
import matplotlib.pyplot as pp

def sor( A, b, x = None, w = 1.0, tol = 1.0e-6, return_niter = False ):
    
    if x is None:
        x = np.random.normal( size = A.shape[ 1 ] )
    
    stop = False
    
    niter = 0
    
    while not stop:
        
        x_next = np.empty( x.shape )
        for i in range( x.shape[ 0 ] ):
            x_next[ i ] = ( 1.0 - w ) * x[ i ] + w * ( 
                b[ i ] - \
                np.sum( A[ i, : i ] * x_next[ : i ] ) - \
                np.sum( A[ i, i + 1 : ] * x[ i + 1 : ] )
            ) / A[ i, i ]
        
        stop = ( np.linalg.norm( A @ x_next - b ) <= tol )
        
        x = x_next
        
        niter = niter + 1
        
    if not return_niter:
        return x
    else:
        return( x, niter )

( x_sor, niter_sor ) = sor( A, b, w = 1.0, return_niter = True )

print( niter_sor )

print( np.max( np.abs( A @ x_sor - b ) ) )
print( np.max( np.abs( A @ x - b ) ) )