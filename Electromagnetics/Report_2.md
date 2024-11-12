# يحيى مدحت يوسف يوسف
# ID: 22011360
To get the potential difference of between $a$ and $b$:  
$$V_{ab} = -\int_a^b \vec{E}.\vec{dr}$$  
Since $\vec{E}$ and $\vec{r}$ are in the same direction:
$$\begin{aligned}  
\therefore V_{ab} & = -\int_b^a \frac{Q}{4\pi \varepsilon_\circ \varepsilon_d r^2}dr \\  
& = \int_a^b \frac{Q}{4\pi \varepsilon_\circ (0.25 r) r^2}dr \\  
& = \int_a^b \frac{Q}{\pi \varepsilon_\circ r^3}dr \\  
& = \frac{Q}{\pi \varepsilon_\circ}\int_a^b \frac{1}{r^3}dr \\  
& = \frac{Q}{\pi \varepsilon_\circ} \left[\frac{-1}{2r^2}\right]_a^b = \frac{Q}{2\pi \varepsilon_\circ} \left[\frac{1}{a^2} - \frac{1}{b^2}\right] \\  
\end{aligned}$$  
So the capacitance will be given in general as following:  
$$\begin{aligned}  
C & = \left|\frac{Q}{V_{ab}}\right| \\  
& = \left|\frac{Q}{\frac{Q}{2\pi \varepsilon_\circ}\left[\frac{1}{a^2} - \frac{1}{b^2}\right]} \right| \\  
& = \left| \frac{2\pi \varepsilon_\circ}{\left[\frac{1}{a^2} - \frac{1}{b^2}\right]} \right|  
\end{aligned}$$  
And for the given radii, the capacitance is:  
$$= \left| \frac{2\pi \varepsilon_\circ}{\left[\frac{1}{(0.01)^2} - \frac{1}{(0.06)^2}\right]}\right| = 5.72 \times 10^{-15}\ \mathrm{F}$$  
To get the $V_\text{max}$ that could be applied to the capacitor, we obtain the maximum electrical charge as follows:  
$$\begin{aligned}  
& E_\text{max} (4\pi r^2)= \frac{Q_\text{max}}{\varepsilon_\circ (0.25 r)}\\  
& Q_\text{max} = 10^6 \times \pi \times \varepsilon_\circ \times (0.01)^3 \mathrm{C}\\  
& = 2.78 \times 10^{-11}\mathrm{C}\\  
& \therefore V_\text{max}= \frac{Q_\text{max}}{C} = 4860.14\ \mathrm{V}  
\end{aligned}$$
