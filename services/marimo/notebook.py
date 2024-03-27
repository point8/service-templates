import marimo

__generated_with = "0.3.4"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    import plotly.express as px
    from vega_datasets import data
    return data, mo, px


@app.cell
def __(mo):
    mo.md("This is a small marimo example")
    return


@app.cell
def __(mo):
    x = mo.ui.slider(start=0, stop=10, step=1)
    x
    return x,


@app.cell
def __(data, mo, px):
    _plot = px.scatter(
        data.cars(),
        x="Horsepower",
        y="Miles_per_Gallon",
        color="Origin"
    )

    plot = mo.ui.plotly(_plot)
    return plot,


@app.cell
def __(mo, plot):
    mo.hstack([plot, plot.value])
    return


if __name__ == "__main__":
    app.run()
