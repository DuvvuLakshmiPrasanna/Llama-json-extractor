# Contributing to Llama JSON Extractor

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Create a branch** for your work (`git checkout -b feature/your-feature`)
4. **Make changes** and commit with clear messages
5. **Push to your fork** and create a Pull Request

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Follow the project's coding standards
- Respect others' time and effort

## How to Contribute

### Bug Reports

- Use GitHub Issues with label `bug`
- Include minimal reproducible example
- Provide system information (Python version, OS, GPU/CPU)
- List steps to reproduce the issue

### Feature Requests

- Use GitHub Issues with label `enhancement`
- Clearly describe the use case
- Explain why this feature would be useful
- Provide example usage if applicable

### Documentation Improvements

- Fix typos, clarity issues, or outdated information
- Add examples or clarifications
- Improve diagrams or structure
- Update references and links

### Code Contributions

**Philosophy**:

- Keep changes focused and minimal
- Maintain backward compatibility
- Add tests for new functionality
- Update documentation accordingly
- Follow PEP 8 style guidelines

**Process**:

1. Create a feature branch
2. Implement your change
3. Add or update tests
4. Run tests locally: `pytest tests/`
5. Update README if needed
6. Submit Pull Request with clear description

## Testing

```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_extraction.py

# Run with coverage
pytest --cov=src tests/
```

## Improving Model Performance

If you discover improvements to the model or training:

1. Document your methodology
2. Provide baseline vs new metrics
3. Share training data additions (if suitable)
4. Add results to `eval/` directory
5. Submit with detailed analysis

## Documentation Standards

- Use clear, concise language
- Include code examples where helpful
- Add links to related documentation
- Use Markdown formatting consistently
- Update Table of Contents for large docs

## Commit Message Format

Follow conventional commits:

```
type(scope): brief description

body (if needed)
- Additional details
- More context
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Example:

```
feat(inference): add batch processing support

- Implement batch_extract() function
- Support multiple invoices in single call
- Add performance benchmarks in tests
```

## Pull Request Process

1. **Title**: Clear, descriptive (follows commit format)
2. **Description**:
   - What changes? Why?
   - Link to related issues
   - Include motivation/context
3. **Tests**: All tests pass
4. **Documentation**: Updated as needed
5. **Review**: Wait for maintainer feedback

**PR Template**:

```markdown
## Description

Brief description of changes

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Documentation improvement
- [ ] Performance improvement

## Related Issues

Closes #(issue number)

## Testing

Describe testing performed

## Checklist

- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] Tests pass locally
```

## Development Environment

```bash
# Clone and setup
git clone https://github.com/DuvvuLakshmiPrasanna/Llama-json-extractor.git
cd Llama-json-extractor
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For testing/linting

# Pre-commit hooks (optional)
pre-commit install
```

## Areas for Contribution

**High Priority**:

- [ ] Additional test cases and edge cases
- [ ] Performance optimizations
- [ ] Language support and localization
- [ ] Documentation translations

**Medium Priority**:

- [ ] UI/UX improvements for Gradio interface
- [ ] Additional schema types
- [ ] Error message improvements
- [ ] API endpoint development

**Lower Priority**:

- [ ] Example notebooks
- [ ] Video tutorials
- [ ] Blog posts on methodology
- [ ] Community benchmarks

## Questions?

- **GitHub Issues**: For technical questions
- **GitHub Discussions**: For general questions and ideas
- **Pull Requests**: For specific code contributions

## License

By contributing, you agree your contributions are licensed under the same MIT license as the project.

---

**Thank you for contributing to make this project better!** 🎉
