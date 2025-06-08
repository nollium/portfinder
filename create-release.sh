#!/bin/bash

# Script to create a new release

if [ -z "$1" ]; then
    echo "Usage: ./create-release.sh <version>"
    echo "Example: ./create-release.sh 1.0.0"
    echo ""
    echo "This will create and push a tag v<version> which triggers the release workflow"
    exit 1
fi

VERSION=$1
TAG="v$VERSION"

# Check if tag already exists
if git rev-parse "$TAG" >/dev/null 2>&1; then
    echo "Error: Tag $TAG already exists!"
    exit 1
fi

echo "Creating release $TAG..."

# Create and push tag
git tag -a "$TAG" -m "Release $TAG"
git push origin "$TAG"

echo ""
echo "✅ Tag $TAG created and pushed!"
echo ""
echo "🚀 The GitHub Actions workflow will now:"
echo "   1. Build binaries for Linux, Windows, and macOS"
echo "   2. Create a GitHub release"
echo "   3. Upload the binaries to the release"
echo ""
echo "You can monitor the progress at:"
echo "https://github.com/<your-username>/<your-repo>/actions"