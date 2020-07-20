from django.shortcuts import render

# Create your views here

import matplotlib.pyplot as Iperf
import io
import urllib, base64

def home(request):
  x = [1]
  y = [2]
  z = [3]
  w = [4]

  l = [0,1,2,3,4]
  xi = list(range(len(l)))

  bA = [24.9,24.9,20.9,21.2,21.6,21.6,20.7,20.7,17.3,17.4,21.9,22.0,24.3,24.3,24.5,24.5,21.9,21.9,20.7,20.8]
  cA = [14.9,14.6,14.4,13.7,13.9,13.9,14.1,14.2,14.3,12.7,12.9,13.0,13.5,13.4,13.5,15.5,15.7,15.7,14.8,14.7,14.8,14.6,14.8,14.8,14.9,14.9,14.7,15.5,15.6,15.6]
  dA = [11.3,11.3,11.5,11.5,11.7,11.7,11.8,11.9,11.4,11.4,11.6,11.6,11.7,11.7,11.8,11.9,11.9,11.9,12.0,12.1,11.7,11.7,11.9,11.9,10.9,11.0,11.1,11.1,10.2,10.2,10.3,10.4,10.5,10.6,10.6,10.6,11.2,11.2,11.4,11.4]

  a = [61.5,61.8,61.8,61.6,61.3,61.7,61.8,61.9,61.8,61.7]
  b = [49.8,42.1,43.2,41.4,34.7,43.9,48.6,49.0,43.8,41.5]
  c = [43.9,41.5,42.6,38.6,40.4,46.9,44.3,44.2,44.5,46.7]
  d = [45.6,47.1,46.0,47.1,47.9,47.2,44.1,41.1,42.3,45.2]

  avg1 = statistics.mean(a)

  avg2 = statistics.mean(b)
  avg2b = statistics.mean(bA)
  bar1 = [avg2b]

  avg3 = statistics.mean(c)
  avg3c = statistics.mean(cA)
  bar2 = [avg3c]
  total = avg3c + avg3c

  avg4 = statistics.mean(d)
  avg4d = statistics.mean(dA)
  bar3 = [avg4d]
  total1 = avg4d + avg4d
  total2 = avg4d + avg4d + avg4d

  Iperf.xticks(xi,l)
  Iperf.bar(x,avg1,color=(1.0, 0.0, 0.0, 1.0))

  Iperf.bar(y,avg2,color=(1.0, 0.0, 0.0, 1.0))

  Iperf.bar(z,avg3,color=(1.0, 0.0, 0.0, 1.0))

  Iperf.bar(w,avg4,color=(1.0, 0.0, 0.0, 1.0))

  Iperf.title("Average Throughput for Concurrent Connections")
  Iperf.xlabel("Number of Concurrent Connections")
  Iperf.ylabel("Average Throughput(Gbits/sec) per Concurrent Connection")
  fig = Iperf.gcf()
  #convert graph into dtring buffer and then we convert 64 bit code into image
  buf = io.BytesIO()
  fig.savefig(buf,format='png')
  buf.seek(0)
  string = base64.b64encode(buf.read())
  uri =  urllib.parse.quote(string)
  return render(request,'home.html',{'data':uri})
