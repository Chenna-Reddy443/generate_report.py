import matplotlib.pyplot as plt

def create_chart(data):
    keys = list(data.keys())[:2]
    values = list(data.values())[:2]

    plt.figure(figsize=(6, 4))
    plt.bar(keys, values, color=['skyblue', 'lightgreen'])
    plt.title('Weather Stats')
    plt.savefig('weather_chart.png')
