# Report 1
يحيى مدحت يوسف يوسف: 22011360
### Question 1
The space between the two half rings of radii $5m$ and $10m$ as shown in Figure, is filled with a surface charge density $\rho = 2\times 10^{-4}r\ C/m^2$. Apply Coulomb's law to find the electric field intensity $\bar{E}$ at the origin.

### Solution:
Considering an infinitesimal area $r\ d\theta\ dr$ whose electric field at the origin is:
$$ d\vec{E} = \frac{r\ d\theta\ dr \rho}{4\pi \epsilon_\circ r^2} \vec{a} $$
, Where $\vec{a}$ is a unit vector in the direction of the electric field.
Integrating: $\int d\vec{E} = \int_{0}^{\pi}\int_{5}^{10}\frac{r\ d\theta\ dr \rho}{4\pi \epsilon_\circ r^2} \vec{a}$
$\because$ the horizontal components will cancel out, so we will only consider the vertical components, and consider the symmetry for each half of the area, let the integral be:
$$\int d\vec{E} = -2\int_{0}^{\frac{\pi}{2}}\int_{5}^{10}\frac{r\ d\theta\ dr \rho}{4\pi \epsilon_\circ r^2}\sin(\theta) \hat{j}$$
$$\vec{E} = \frac{-2 \times 2\times 10^{-4}}{4\pi \epsilon_\circ}\hat{j}\int_{0}^{\frac{\pi}{2}}\int_{5}^{10}\frac{r^2\ d\theta\ dr}{r^2}\sin(\theta)$$
$$\vec{E} = -\frac{\cancel{4}\times 10^{-4}}{\cancel{4}\pi \epsilon_\circ} \hat{j}\int_{0}^{\frac{\pi}{2}}\int_{5}^{10}\frac{\cancel{r^2}\ d\theta\ dr}{\cancel{r^2}}\sin(\theta)$$
$$\vec{E} = -\frac{10^{-4}}{\pi \epsilon_\circ} \hat{j}\int_{0}^{\frac{\pi}{2}}\int_{5}^{10}\sin(\theta) d\theta\ dr$$
$$\vec{E} = -\frac{10^{-4}}{\pi \epsilon_\circ} \hat{j}\left[r\right]_{5}^{10}\left[-\cos(\theta)\right]_{0}^{\frac{\pi}{2}}$$
$$\vec{E} = -\frac{10^{-4}}{\pi \epsilon_\circ} \hat{j}(5) = -17975103.58\ \hat{j}$$

### Question 2
Three spherical shells of radii $1, 2$ and $3m$, centered at the origin, The space $1<r<2$ is filled with a volume charge distribution of volume charge density $\rho_v = 4\times 10^{-4}\ C/m^3$. The space $2<r<3$ is a conducting material. A surface charge distribution of density $\rho_s = 2\times 10^{-4}\ C/m^2$ is distributed over the shell of radius $3m$. Apply Gauss's law to find the electric flux density $\bar{D}$ everywhere.

### Solution:
Gauss's law: $E \times A = \LARGE\frac{Q_{enclosed}}{\epsilon_\circ}$
$\therefore E * 4\pi r^2  = \LARGE\frac{Q_{enclosed}}{\epsilon_\circ}$
$\because$ For $r<1: Q_{enclosed} = 0, \therefore \bar{D} = 0 C/m^2$
___
$\because$ For $1<r<2: Q_{enclosed} = 4\times 10^{-4} \times \frac{4}{3} \pi \times r^3$
$\because \bar{D} = \bar{E} \times \epsilon_{\circ} = \Large{\frac{Q_{enclosed}}{A}} = \large\frac{4\times 10^{-4} \times \frac{1}{3} \times \cancel{4\pi r^2} r}{\cancel{4\pi r^2}}$
$\therefore \bar{D} = \large\frac{4\times 10^{-4}}{3}(r - 1)C/m^2$
___
$\because$ For $2<r\leq 3: Q_{enclosed} = 4\times 10^{-4} \times \frac{4}{3} \pi \times 8$
$\therefore \bar{D} = \frac{32\times 10^{-4} \times \frac{1}{3} \times\cancel{4\pi}}{\cancel{4\pi} R^2}$$= \frac{32\times 10^{-4}}{3 R^2} C/m^2$
___
$\because$ For $r\gt 3: Q_{enclosed} = 4\times 10^{-4} \times \frac{4}{3} \pi \times 8 + 4\pi (3)^2 \times 2\times 10^{-4}$
$\therefore \bar{D} = \frac{4\times 10^{-4} \times \frac{4}{3} \pi \times 8 + 4\pi (3)^2 \times 2\times 10^{-4}}{4\pi R^2}$
$\therefore \bar{D} = \frac{(4 \times \frac{1}{3} \times 8 +  (3)^2 \times 2) \times 10^{-4}}{\cancel{4\pi} R^2}\cancel{4\pi}$
$\therefore \bar{D} = \frac{(\frac{32}{3}+  18) \times 10^{-4}}{R^2} = \frac{86 \times 10^{-4}}{3R^2}$
