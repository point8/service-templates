# Service Templates

![logo.png](logo.png)

_(Public mirror: https://github.com/point8/service-templates)_

## Run your own TLS secured data (visualization) service with docker

Running your [streamlit](https://streamlit.io/), [voila](https://voila.readthedocs.io/en/stable/index.html), [dash](https://dash.plotly.com/), [FastAPI](https://fastapi.tiangolo.com), [AlpineJS](https://alpinejs.dev/), or [svelte](https://svelte.dev) app as a cloud service with a simple password authentication and secured by HTTPS.

The repository consists of example apps and a reverse proxy to automatically handle the HTTPS endpoint and TLS certificates. Everything is glued together and deployed using [`docker-compose`](https://docs.docker.com/compose/).

Additionally NoSQL and SQL database services are available and a Redis service is configured too if one is needed

If you want to quickstart your development you can use [pocketbase.io](https://pocketbase.io/) as a backend.

The service gets automatically deployed using [`ansible`](https://docs.ansible.com/ansible/latest/index.html) from inside the GitLab CI.

## Documentation

Either have a look into our internal [documentation](https://ccauet.point8.work/service-templates) or build the documention yourself:
```
pushd docs && poetry run mkdocs build && open build/index.html && popd
```

## Smart Erosion & AutoPlan

Point 8 is a partner in the research project SmartErosion. This tool was created as part of the research project. The project was supported by funds from the __European Regional Development Fund (ERDF) 2014-2020 "Investment for Growth and Jobs"__.

The project was further developed and improved in the research project AutoPlan. The AutoPlan project was funded by the __Central Innovation Program for SMEs (Zentrale Innovationsprogramm Mittelstand – ZIM) of the German Federal Ministry of Economics and Climate Protection__.

<p float="middle">
  <img src="Ziel2NRW_RGB_1809_jpg.jpg" width="38%" />
  <img src="bmwi.png" width="18%" />
  <img src="zim.png" width="10%" />
  <img src="EFRE_Foerderhinweis_englisch_farbig.jpg" width="32%" />
</p>
