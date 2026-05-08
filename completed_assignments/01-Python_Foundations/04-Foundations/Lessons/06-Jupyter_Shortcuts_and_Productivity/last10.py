x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin(x)", linestyle="--", color="blue")
plt.plot(x, y2, label="cos(x)", linestyle=":", color="red")
plt.title("Customized Line Plot")
plt.xlabel("x (radians)")
plt.ylabel("value")
plt.legend()
plt.grid(True)
plt.show()
x = np.linspace(0, 2*np.pi, 100)
y1 = np.tan(x)
y2 = np.tan(x) * 2

plt.plot(x, y1, label="tan(x)", linestyle="--", color="blue")
plt.plot(x, y2, label="tan(x)*2", linestyle=":", color="red")
plt.title("Customized Line Plot")
plt.xlabel("x (radians)")
plt.ylabel("value")
plt.legend()
plt.grid(True)
plt.show()
#Show the last 10 commands in this session
%history -n -10
%save last10.py -n -10
%history -n 1-5  # Show the first 5 commands in this session
# Save history to a file
%save my_session.py 1-5
#Show the last 10 commands in this session
%history -n -10
%save last10.py -n -10
#Show the last 10 commands in this session
%history -n -10
%save last10.py -10
#Show the last 10 commands in this session
%history -n -10
%save last10.py -n -10
#Show the last 10 commands in this session
%history -n -10
%save last10.py -10
#Show the last 10 commands in this session
%history -n -10
%save last10.py ~1/1-10
