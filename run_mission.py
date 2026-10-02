"""Запуск: python run_mission.py --days 6 --seed 42"""
import argparse, sched, time
from mission import delta_v, flight_time, fuel_needed, random_event

def build_parser():
    p = argparse.ArgumentParser(description="Симулятор межпланетной миссии")
    p.add_argument("--days",  type=int,   default=5,   help="длительность миссии, сут")
    p.add_argument("--seed",  type=int,   default=None, help="зерно ГСЧ")
    p.add_argument("--speed", type=float, default=0.2, help="секунд на 1 сутки")
    return p

def main():
    args = build_parser().parse_args()
    resource = 100
    s = sched.scheduler(time.time, time.sleep)

    def day_report(day):
        """Отчёт за сутки; при исчерпании ресурса отменяет все задачи."""
        nonlocal resource
        desc, delta = random_event(args.seed + day if args.seed is not None else None)
        resource = max(0, min(100, resource + delta))
        print(f"Сутки {day:>2} | {desc:<38s} {delta:+3d} | ресурс {resource:3d}% "
              f"{'#' * (resource // 5)}")
        if resource == 0:
            for ev in list(s.queue):
                s.cancel(ev)
            return
        if day < args.days:
            s.enter(args.speed, 1, day_report, (day + 1,))
delta_v = 4200
fuel_needed = 15000
flight_time = args.day * 24 * 3600

print('===СТАРТОВЫЙ БЛОК РАСЧЕТОВ===')
print(f'Требуемая Delta-V: {delta_v} м/с')
print(f'Необходимое топливо: {fuel_needed} кг')
print(f'Общее время полета: {args.days} дней ({flight_time} сек)')
print('==============================\n')

if __name__ == "__main__":
    main()
