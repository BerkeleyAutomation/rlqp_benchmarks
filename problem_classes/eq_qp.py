import numpy as np
import scipy.sparse as spa
import cvxpy


class EqQPExample(object):
    '''
    Equality constrained QP example
    '''
    def __init__(self, n, seed=1, create_cvxpy_problem=False, rng=None):
        '''
        Generate problem in QP format and CVXPY format
        '''
        # Set random seed
        if rng is None:
            rng = np.random.default_rng(seed)

        m = int(n/2)

        # Generate problem data
        self.n = int(n)
        self.m = m
        P = spa.random(n, n, density=0.15,
                       random_state=rng,
                       data_rvs=rng.standard_normal,
                       format='csc')
        self.P = P.dot(P.T).tocsc() + 1e-02 * spa.eye(n)
        self.q = rng.standard_normal(n)
        self.A = spa.random(m, n, density=0.15,
                            data_rvs=np.random.randn,
                            format='csc')
        x_sol = rng.standard_normal(n)  # Create fictitious solution
        self.l = self.A@x_sol
        self.u = np.copy(self.l)

        self.qp_problem = self._generate_qp_problem()
        if create_cvxpy_problem:
            self.cvxpy_problem = self._generate_cvxpy_problem()

    @staticmethod
    def name():
        return 'Eq QP'

    def _generate_qp_problem(self):
        '''
        Generate QP problem
        '''
        problem = {}
        problem['P'] = self.P
        problem['q'] = self.q
        problem['A'] = self.A
        problem['l'] = self.l
        problem['u'] = self.u
        problem['m'] = self.A.shape[0]
        problem['n'] = self.A.shape[1]

        return problem

    def _generate_cvxpy_problem(self):
        '''
        Generate QP problem
        '''
        x_var = cvxpy.Variable(self.n)
        objective = .5 * cvxpy.quad_form(x_var, self.P) + self.q * x_var
        constraints = [self.A * x_var == self.u]
        problem = cvxpy.Problem(cvxpy.Minimize(objective), constraints)

        return problem

    def revert_cvxpy_solution(self):
        '''
        Get QP primal and duar variables from cvxpy solution
        '''

        variables = self.cvxpy_problem.variables()
        constraints = self.cvxpy_problem.constraints

        # primal solution
        x = variables[0].value

        # dual solution
        y = constraints[0].dual_value

        return x, y
