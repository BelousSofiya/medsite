module.exports = {
  'env': {
    'node': true,
    'jest': true,
    'browser': true,
    'es2021': true
  },
  'extends': ['eslint:recommended', 'plugin:react/recommended', 'plugin:react-hooks/recommended'],
  'parserOptions': {
    'ecmaVersion': 12,
    'sourceType': 'module',
    'ecmaFeatures': {
      'jsx': true
    }
  },
  'plugins': ['react', 'react-hooks'],
  'rules': {
    'react/react-in-jsx-scope': 'off',
    'react/prop-types': 'warn',
    'max-len': [
      'warn',
      {
        'code': 120,
        'ignoreTemplateLiterals': true
      }
    ],
    'linebreak-style': [
      'error',
      'unix'
    ],
    'quotes': [
      'error',
      'single'
    ],
    'semi': [
      'error',
      'always'
    ],
    'no-console': [
      'warn',
      {
        'allow': [
          'warn',
          'error',
          'info'
        ]
      }
    ],
    'no-trailing-spaces': 2,
    'jsx-quotes': ['error', 'prefer-double']
  }
};