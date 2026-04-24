# Project 2 Reflection

Name: Ruiqi Huang

Course: EART60702 Earth and Environmental Data Science

Date: 24 April 2026

---

At the beginning, the task seemed quite straightforward: use historical climate data to predict future temperature. However, once I started working with the dataset, it quickly became clear that the problem was more complicated than it looked.

Before this project, I tended to think about relationships between variables in fairly simple terms — a regression line, a slope, a correlation coefficient. That way of thinking assumes the relationship is stable across the dataset, which might work in some cases, but doesn’t really hold for physical systems like climate. Working with this data made that limitation much more obvious.

For example, the relationship between near-surface air temperature (TREFHT) and urban maximum temperature (TREFMXAV_U) is not fixed. It changes depending on conditions like humidity, radiation, and season. In summer, when solar input is higher and surfaces are drier, small changes in TREFHT can lead to much larger increases in TREFMXAV_U than in winter. A single linear model ends up averaging over all these situations, which means it misses the structure that actually matters.

Using XGBoost shifted how our group approached the problem. Instead of asking for a single overall relationship, it became more about understanding when and under what conditions that relationship changes. The difference showed up quite clearly in the results — XGBoost consistently performed better than the linear models under the same setup. That gap suggests the nonlinear interactions in the data are important, and models that can capture them have a clear advantage.

What I take from this is not just that one model performs better than another, but that choosing a model also means making an assumption about how the system works. Comparing linear models with XGBoost made those assumptions more visible, rather than leaving them implicit.

Another part I found useful was looking at the results from different angles — over time, across seasons, and across locations. This helped me move beyond just reporting metrics like RMSE and think more carefully about what the model is actually capturing.