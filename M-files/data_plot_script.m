clear all
load mama.dat
t = mama(:,1);
x = mama(:,2);
y = mama(:,3);
z = mama(:,4);
subplot(2,2,1)
plot3(x,y,z,'k.');
subplot(2,2,2)
plot(t,x,'k.');
title('Time-series for x1');
subplot(2,2,3)
plot(t,y,'k.');
title('Time-series for x2');
subplot(2,2,4)
plot(t,z,'k.');
title('Time-series for x3');
%xlim([-0.5,2.0]);
%xlabel('q-state');
%ylim([-1.5,1.5]);
%ylabel('p-state');
hold on;
