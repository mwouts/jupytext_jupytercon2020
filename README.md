# Jupytext at JupyterCon 2020

On October 13, 2020 I was glad to give a talk on [Jupytext](https://github.com/mwouts/jupytext) at the [JupyterCon 2020](https://cfp.jupytercon.com/2020/schedule/) conference.

My talk is now available on the [JupyterCon Youtube Channel](https://www.youtube.com/c/JupyterCon/) - together with all the other talks from the conference!

[![Youtube ](https://img.youtube.com/vi/SDYdeVfMh48/0.jpg)](https://www.youtube.com/watch?v=SDYdeVfMh48)

The slides are available at [`slides.md`](slides.md), in the form of a Markdown file that you can also open in Jupyter as a notebook. Here is an export of the notebook as [HTML slides](https://mwouts.github.io/jupytext_jupytercon2020/slides.html).

The HTML version of the slide deck was generated & updated automatically using this [pre-save hook](https://gist.github.com/mwouts/04a6dfa571bda5cc59fa1429d130998f). And the talk itself was recording using [OBS Studio](https://obsproject.com/).

Let me thank the many people who supported me in the process of writing and recording this talk: Florent Zara, Eric Lebigot and Emmanuel Serie at CFM, as well as my brother François, and my kids and my wife at home.

## Talk summary

Did you ever dream of editing your Jupyter Notebooks outside of Jupyter? Jupytext lets you synchronize your notebooks with `.py` or `.md` versions. These alternative formats are way lighter than `.ipynb`, and are a perfect fit for version control and collaboration. Edit the `.py` or `.md` files in a text editor, and Jupytext will automatically apply the changes back to the `.ipynb` file.

Talk outline
- Why Jupytext: going further than the `.ipynb` format
- Jupytext's approach: use Jupyter Notebooks, but store them as `.py` or `.md` files
- Demo: How a `.py` file becomes a notebook!
- Paired notebooks: `.py` notebook with persistent outputs
- What you can do with Jupytext: Version control, Write notebooks as text, Refactor notebooks, QA on notebooks
- Which Jupytext format for which usage?
- Awesome projects that use Jupytext
- Links, facts & figures

## How to follow the demo locally

Clone the repository with 
```
git clone https://github.com/mwouts/jupytext_jupytercon2020.git
```

Change directory, create and activate the `jupytext-demo` environment with
```
cd jupytext_jupytercon2020
conda env create --file environment.yml
conda activate jupytext-demo
```

Install the plotly extensions for JupyterLab with
```
jupyter labextension install jupyterlab-plotly@4.9.0
jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget@4.9.0
```

And then start Jupyter Lab with
```
jupyter lab
```
and enjoy the demo!
