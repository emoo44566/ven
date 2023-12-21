import pandapower as pp
import pandapower.networks as nw
import pandapower.plotting as plot

# ساخت یک مدل از شبکه 14 حالته IEEE با استفاده از کتابخانه pandapower
net = nw.mv_oberrhein()

# افزودن بارها به شبکه
pp.create_load(net, 2, p_mw=0.1, q_mvar=0.05)
pp.create_load(net, 4, p_mw=0.2, q_mvar=0.1)

# اجرای شبیه‌سازی قدرت
pp.runpp(net)

# نمایش شبکه
plot.simple_plot(net)