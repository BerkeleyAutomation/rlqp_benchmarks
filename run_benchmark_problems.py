'''
Run all benchmarks for the OSQP paper

This code tests the solvers:
    - OSQP
    - GUROBI
    - MOSEK
    - ECOS
    - qpOASES

'''
from benchmark_problems.example import Example
import solvers.solvers as s
from utils.general import gen_int_log_space
from utils.benchmark import get_cumulative_data, compute_performance_profiles

# Define solvers to benchmark
solvers = [
            # s.OSQP,
            # s.OSQP_polish,
            s.GUROBI,
            s.MOSEK,
            s.ECOS,
            s.qpOASES
           ]

settings = {
             # s.OSQP: {'polish': False},
             # s.OSQP_polish: {'polish': True},
             s.GUROBI: {},
             s.MOSEK: {},
             s.ECOS: {},
             s.qpOASES: {'nWSR': 1000000,    # Number of working set recalcs
                         'cputime': 1000.     # Seconds (N.B. Must be float!)
                         }
            }

# Number of instances per different dimension
n_instances = 10

# Shut up solvers
for key in settings:
    settings[key]['verbose'] = False

# Run benchmark problems
problems = [
            'Random QP',
            'Eq QP',
            'Portfolio',
            'Lasso',
            'SVM',
            'Huber',
            'Control'
            ]

problem_dimensions = {'Random QP': gen_int_log_space(10, 2000, 20),
                      'Eq QP': gen_int_log_space(10, 2000, 20),
                      'Portfolio': gen_int_log_space(5, 150, 20),
                      'Lasso': gen_int_log_space(10, 200, 20),
                      'SVM': gen_int_log_space(10, 200, 20),
                      'Huber': gen_int_log_space(10, 200, 20),
                      'Control': gen_int_log_space(4, 100, 20)}

# Some problems become too big to be executed in parallel and we solve them
# serially
problem_parallel = {'Random QP': True,
                    'Eq QP': True,
                    'Portfolio': True,
                    'Lasso': True,
                    'SVM': True,
                    'Huber': True,
                    'Control': True}

# Small dimensions (to comment when running on the server)
for key in problem_dimensions:
    problem_dimensions[key] = [4, 5]

# Run all examples
for problem in problems:
    example = Example(problem,
                      problem_dimensions[problem],
                      solvers,
                      settings,
                      n_instances)
    example.solve(parallel=problem_parallel[problem])


# Collect cumulative data for each solver
get_cumulative_data(solvers, problems)

# Compute performance profiles
compute_performance_profiles(solvers)
