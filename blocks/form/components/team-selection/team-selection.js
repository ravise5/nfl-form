import { createOptimizedPicture } from '../../../../scripts/aem.js';

/**
 * Decorates a custom form field component
 * @param {HTMLElement} element - The DOM element containing the field wrapper.
 * @param {Object} fieldJson - The form json object for the component.
 * @param {HTMLElement} parentElement - The parent element of the field.
 * @param {string} formId - The unique identifier of the form.
 */
export default async function decorate(element, fieldJson, parentElement, formId) {
  const { enumNames: imagePaths, enum: altText } = fieldJson;
  const { selectionType } = fieldJson.properties;

  element.classList.add('team-selection');

  // single or multi selection
  if (selectionType === 'single') {
    element.querySelectorAll('input').forEach((input) => {
      input.type = 'radio';
    });
  } else if (selectionType === 'multi') {
    element.querySelectorAll('input').forEach((input) => {
      input.type = 'checkbox';
    });
  }

  element.querySelectorAll('.checkbox-wrapper').forEach((wrapper, index) => {
    const image = createOptimizedPicture(imagePaths[index], altText[index]);
    wrapper.appendChild(image);
  });
}
