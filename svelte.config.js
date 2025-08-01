import adapter from '@sveltejs/adapter-static';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		// adapter-auto only supports some environments, see https://svelte.dev/docs/kit/adapter-auto for a list.
		// If your environment is not supported, or you settled on a specific environment, switch out the adapter.
		// See https://svelte.dev/docs/kit/adapters for more information about adapters.
		adapter: adapter({
			pages: './docs',
			assets: './docs',
			fallback: 'index.html',
			precompress: false,
			strict: true
		}),
		paths: {
			base: "/golden-sun-guide"
		}
	}
};

export const prerender = true;
export default config;
