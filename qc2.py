from qiskit import QuantumCircuit,  QuantumRegister
from qiskit.quantum_info import Statevector
from math import pi
import qiskit
import numpy as np

def figure_it_out_1():
    """ Implement a function that passes the test, using  a quantum circuit and gates only

    Args: 
        None
    """
    q = QuantumRegister(2, name='q')
    qc = QuantumCircuit(q, name='qc')

    qc.x(q[0])
    qc.h(q)
    qc.swap(q[1], q[0])

    return Statevector(qc)


def figure_it_out_2():
    """ Implement a function that passes the test, using  a quantum circuit and gates only

    Args: 
        None
    """
    q = QuantumRegister(2, name='q')
    qc = QuantumCircuit(q, name='qc')

    qc.x(q)
    qc.h(q)
    qc.cx(q[1], q[0])

    return Statevector(qc)


def figure_it_out_3():
    """ Implement a function that passes the test, using  a quantum circuit and gates only

    Args: 
        None
    """
    q = QuantumRegister(2, name='q')
    qc = QuantumCircuit(q, name='qc')

    qc.x(q[0])
    qc.h(q)
    qc.cx(q[1], q[0])

    return Statevector(qc)


def figure_it_out_4():
    """ Implement a function that passes the test, using  a quantum circuit and gates only

    Args: 
        None
    """
    q = QuantumRegister(2, name='q')
    qc = QuantumCircuit(q, name='qc')
    
    qc.h(q[1])
    qc.x(q[0])
    qc.cx(q[1],q[0])

    return Statevector(qc)

    
def figure_it_out_5(v):
    """ Implement a function that passes the test, by creating a matrix that transform the
        following inputs into the following outputs. You dont need qiskit for this,
        only numpy, such as np.matrix(...)

        input   output 
          |00> : |11>
          |01> : |10>
          |10> : |00>
          |11> : |01>

    Args: 
        vector that is multiplied by the matrix
    """
    transform_matrix = np.matrix([
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0]
    ])

    return np.dot(v, transform_matrix)


def figure_it_out_6(v):
    """ Implement a function that passes the test, by creating a matrix that transform the
        following inputs into the following outputs. Yoy dont need qiskit for this,
        only numpy, such as np.matrix(...)

          input   output 
          |001> : |111>
          |011> : |010>
          |110> : |011>
          |111> : |101>

    Args: 
        vector that is multiplied by the matrix
    """
    transform_matrix = np.matrix([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0]
    ])

    return np.dot(v, transform_matrix)


def figure_it_out_7(init_vector):
    """ Implement a function that passes the tests. Use qiskit 'initialize'
        and then gates
    Args: 
        init_vector
    """
    qc = QuantumCircuit(2, name='qc')

    qc.initialize(init_vector)
    qc.cx(qc.qregs[0][0], qc.qregs[0][1])

    return Statevector(qc)


def figure_it_out_8(init_vector):
    """ Implement a function that passes the tests. Use qiskit 'initialize' 
        and then gates
    Args: 
        init_vector
    """
    qc = QuantumCircuit(3)

    qc.initialize(init_vector)

    qc.h(qc.qregs[0])
    qc.cx(qc.qregs[0][0], qc.qregs[0][1])

    return Statevector(qc)
