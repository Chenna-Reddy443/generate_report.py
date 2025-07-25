from fetch_data import fetch_weather
from analyze_data import process_weather
from visualize import create_chart
from generate_report import create_pdf

def main():
    raw = fetch_weather()
    processed = process_weather(raw)
    create_chart(processed)
    create_pdf(processed)

if __name__ == "__main__":
    main()
