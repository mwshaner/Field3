import numpy as np
import matplotlib.pyplot as plt
from collections import namedtuple
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# Define a simple Vec3 type
Vec3 = namedtuple('Vec3', ['x', 'y', 'z'])

class Field3:
    def __init__(self, P, Q, R):
        """
        Initializes the Field3 object with functions P, Q, and R.

        Args:
            P (callable): Function taking a Vec3 and returning the x-component.
            Q (callable): Function taking a Vec3 and returning the y-component.
            R (callable): Function taking a Vec3 and returning the z-component.
        """
        self.P = P
        self.Q = Q
        self.R = R

    def get(self, pos):
        """
        Computes and returns a Vec3 whose components are given by evaluating
        the functions m_P, m_Q, and m_R at the given position.

        Args:
            pos (Vec3): A point in space.

        Returns:
            Vec3: The vector at that point.
        """
        return Vec3(
            self.P(pos),
            self.Q(pos),
            self.R(pos)
        )

# Define the helix vector field functions.
# These functions produce a field whose integral curves form a counter-clockwise helix around the x-axis.
def P(pos):
    # Constant forward motion along the x-axis.
    return -1

def Q(pos):
    # y-component is -z.
    return -pos.z

def R(pos):
    # z-component is y.
    return pos.y

# Create an instance of Field3 with the helix functions.
field = Field3(P, Q, R)

# Create a 3D grid of points.
n = 6  # number of points per axis (adjust for finer/coarser grid)
x = np.linspace(-5, 5, n)
y = np.linspace(-5, 5, n)
z = np.linspace(-5, 5, n)
X, Y, Z = np.meshgrid(x, y, z)

# Allocate arrays for the vector components.
U = np.zeros(X.shape)
V = np.zeros(Y.shape)
W = np.zeros(Z.shape)

# Evaluate the vector field at each grid point.
for index, _ in np.ndenumerate(X):
    pos = Vec3(X[index], Y[index], Z[index])
    vec = field.get(pos)
    U[index] = vec.x
    V[index] = vec.y
    W[index] = vec.z

# Plot the 3D vector field using matplotlib's quiver.
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Adjust 'length' to control arrow size.
ax.quiver(X, Y, Z, U, V, W, length=2.0, normalize=True, color='b')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Propwash Vector Field')
plt.show()
