import datetime
from rich.console import Console
from rich.table import Table
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.types import Dates, String, Integers
from sqlalchemy import Column, create_engine
from sqlalchemy.sql import extract
import typer


app = typer.Typer()
Base = declarative_base()
engine = create_engine(r'sqlite:///database/diary.sqlite',echo=True)


class diary(Base):
    __tablename__ = 'diary'

    id = Column(Integer,primary_key=True,autoincrement='auto')
    log = Column(String)
    date = Column(Date)
    
    def __init__(self,log,date):
        self.log = log
        self.date = date


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

#declaring commands 
@app.command()
def add():
    text = typer.prompt('log')
    session.add(diary(texg,datetime.date.today()))
    session.commit()

@app.command()
def all():
    x = session.query(diary).all()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Date", style="dim", width=12)
    table.add_column("log")
    for i in x:
        y=i.date
        table.add_row('{}-{}-{}'.format(y.day,y.month,y.year),i.log)

    console.print(table)


@app.command()
def month():
    mo = typer.prompt('month(number)')
    x = session.query(diary).filter(extract('month',diary.date)==int(mo)).all()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Date", style="dim", width=12)
    table.add_column("log")
    for i in x:
        y=i.date
        table.add_row('{}-{}-{}'.format(y.day,y.month,y.year),i.log)

    console.print(table)


@app.command()
def day():
    year = typer.prompt('year')
    month = typer.prompt('month')
    day = typer.prompt('day')
    x = session.query(diary).filter(extract('month',diary.date)==int(month),extract('day',diary.date)==int(day),extract('year',diary.date)==int(year)).all()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Date", style="dim", width=12)
    table.add_column("log")
    for i in x:
        y=i.date
        table.add_row('{}-{}-{}'.format(y.day,y.month,y.year),i.log)

    console.print(table)


app()