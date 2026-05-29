# bumbleflies.de Redesign (Astro)

This directory contains the new Astro-based website for bumbleflies.de, deployed to `beta.bumbleflies.de`.

## Development

```bash
# Install dependencies
npm install

# Run dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Docker Build

The Dockerfile builds the Astro site and serves it via Nginx:

```bash
docker build -t bumble-beta .
docker run -p 8080:80 bumble-beta
```

## Deployment

The site is automatically built and deployed via GitHub Actions:
- `.github/workflows/build-beta.yml` builds the Docker image
- Image is pushed to `ghcr.io/bumbleflies/bumble-beta`
- Docker Compose pulls the image and serves on `beta.bumbleflies.de`

## Project Structure

```
beta/
├── src/
│   ├── pages/        # Astro pages (become routes)
│   ├── components/   # Reusable Astro components
│   └── styles/       # Global styles
├── public/           # Static assets
├── Dockerfile        # Build image
├── nginx.conf        # Nginx config
└── astro.config.mjs  # Astro configuration
```

For full redesign spec, see `/home/cda/dev/infrastructure/bumbleflies/PROJECT_HANDOFF.md`.
