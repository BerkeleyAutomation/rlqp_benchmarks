from solvers.ecos import ECOSSolver
from solvers.gurobi import GUROBISolver
from solvers.mosek import MOSEKSolver
from solvers.osqp import OSQPSolver
from solvers.qpoases import qpOASESSolver

ECOS = 'ECOS'
GUROBI = 'GUROBI'
OSQP = 'OSQP'
OSQP_high = OSQP + '_high'
OSQP_polish = OSQP + '_polish'
OSQP_polish_high = OSQP_polish + '_high'
MOSEK = 'MOSEK'
qpOASES = 'qpOASES'

# solvers = [ECOSSolver, GUROBISolver, MOSEKSolver, OSQPSolver]
# SOLVER_MAP = {solver.name(): solver for solver in solvers}


SOLVER_MAP = {OSQP: OSQPSolver,
              OSQP_high: OSQPSolver,
              OSQP_polish: OSQPSolver,
              OSQP_polish_high: OSQPSolver,
              GUROBI: GUROBISolver,
              MOSEK: MOSEKSolver,
              ECOS: ECOSSolver,
              qpOASES: qpOASESSolver}

time_limit = 1000. # Seconds

# Solver settings
settings = {
    OSQP: {'polish': False,
           'max_iter': int(1e09),
           'eps_prim_inf': 1e-15,  # Disable infeas check
           'eps_dual_inf': 1e-15,
    },
    OSQP_high: {'eps_abs': 1e-05,
                'eps_rel': 1e-05,
                'polish': False,
                'max_iter': int(1e09),
                'eps_prim_inf': 1e-15,  # Disable infeas check
                'eps_dual_inf': 1e-15
    },
    OSQP_polish: {'polish': True,
                  'max_iter': int(1e09),
                  'eps_prim_inf': 1e-15,  # Disable infeas check
                  'eps_dual_inf': 1e-15
    },
    OSQP_polish_high: {'eps_abs': 1e-05,
                       'eps_rel': 1e-05,
                       'polish': True,
                       'max_iter': int(1e09),
                       'eps_prim_inf': 1e-15,  # Disable infeas check
                       'eps_dual_inf': 1e-15
    },
    GUROBI: {'TIME_LIMIT': time_limit},
    MOSEK: {'MSK_DPAR_OPTIMIZER_MAX_TIME': time_limit},
    ECOS: {},
    qpOASES: {}
}

for key in settings:
    settings[key]['verbose'] = True
    settings[key]['time_limit'] = time_limit
