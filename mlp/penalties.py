import numpy as np

seed = 22102017
rng = np.random.RandomState(seed)


class L1Penalty(object):
    """L1 parameter penalty.

    Term to add to the objective function penalising parameters
    based on their L1 norm.
    """

    def __init__(self, coefficient):
        """Create a new L1 penalty object.

        Args:
            coefficient: Positive constant to scale penalty term by.
        """
        assert coefficient > 0., 'Penalty coefficient must be positive.'
        self.coefficient = coefficient

    def __call__(self, parameter):
        """Calculate L1 penalty value for a parameter.

        Args:
            parameter: Array corresponding to a model parameter.

        Returns:
            Value of penalty term.
        """
<<<<<<< HEAD
        raise NotImplementedError
=======
        return self.coefficient * abs(parameter).sum()
>>>>>>> 226249b7aced1403b9e107cb361e1f4c41fa771d

    def grad(self, parameter):
        """Calculate the penalty gradient with respect to the parameter.

        Args:
            parameter: Array corresponding to a model parameter.

        Returns:
            Value of penalty gradient with respect to parameter. This
            should be an array of the same shape as the parameter.
        """
<<<<<<< HEAD
        raise NotImplementedError
=======
        return self.coefficient * np.sign(parameter)
>>>>>>> 226249b7aced1403b9e107cb361e1f4c41fa771d

    def __repr__(self):
        return 'L1Penalty({0})'.format(self.coefficient)


class L2Penalty(object):
    """L1 parameter penalty.

    Term to add to the objective function penalising parameters
    based on their L2 norm.
    """

    def __init__(self, coefficient):
        """Create a new L2 penalty object.

        Args:
            coefficient: Positive constant to scale penalty term by.
        """
        assert coefficient > 0., 'Penalty coefficient must be positive.'
        self.coefficient = coefficient

    def __call__(self, parameter):
        """Calculate L2 penalty value for a parameter.

        Args:
            parameter: Array corresponding to a model parameter.

        Returns:
            Value of penalty term.
        """
<<<<<<< HEAD
        raise NotImplementedError
=======
        return 0.5 * self.coefficient * (parameter ** 2).sum()
>>>>>>> 226249b7aced1403b9e107cb361e1f4c41fa771d

    def grad(self, parameter):
        """Calculate the penalty gradient with respect to the parameter.

        Args:
            parameter: Array corresponding to a model parameter.

        Returns:
            Value of penalty gradient with respect to parameter. This
            should be an array of the same shape as the parameter.
        """
<<<<<<< HEAD
        raise NotImplementedError

    def __repr__(self):
        return 'L2Penalty({0})'.format(self.coefficient)
=======
        return self.coefficient * parameter

    def __repr__(self):
        return 'L2Penalty({0})'.format(self.coefficient)
>>>>>>> 226249b7aced1403b9e107cb361e1f4c41fa771d
