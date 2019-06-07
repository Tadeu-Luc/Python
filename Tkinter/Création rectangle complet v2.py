from turtle import *

def trace_ligne (xa,ya,xb,yb):
    up()
    goto(xa,ya)
    down()
    goto(xb,yb)

trace_ligne (-350,-250,350,-250)
trace_ligne (350,-250,350,250)
trace_ligne (350,250,-350,250)
trace_ligne (-350,250,-350,-250)

trace_ligne(-350,-250,350,250)
trace_ligne(-350,250,350,-250)
