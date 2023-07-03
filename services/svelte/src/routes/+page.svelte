<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<script>
  let clicked = false;
  let item;

	async function handleClick() {
    clicked = true;

    item = await fetch(`https://localhost/api/random`).then((r) => r.json());
    console.log(item)
	}
</script>

<button on:click|once={handleClick}> Click me </button>

{@debug item}

{#if clicked}
	<p>Connecting to backend...</p>

  <p>{item}</p>
{/if}
