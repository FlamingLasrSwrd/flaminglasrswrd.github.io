/* Clipboard Button */
/* https://www.cssscript.com/copy-text-to-clipboard-with-single-click-clipboard-button/ */
(root, factory) {
   /* istanbul ignore next */
   if (typeof define === 'function' && define.amd) {
       define([], factory);
   } else if (typeof module === 'object' && module.exports) {
       module.exports = factory();
   } else {
       root.clipboardButton = factory();
 }
}(this, function () {

   function createNode(text) {
       var node = document.createElement('textarea');
       node.textContent = text;
       node.style.position = 'absolute';
       node.style.left = '-10000px';
       return node;
   }

   function copyNode(node) {
       var selection = document.getSelection();
       selection.removeAllRanges();

       var range = document.createRange();
       range.selectNodeContents(node);
       selection.addRange(range);

       document.execCommand('copy');
       selection.removeAllRanges();
   }

   function copyText(text) {
       var node = createNode(text);
       document.body.appendChild(node);
       copyNode(node);
       document.body.removeChild(node);
   }

   function clipboardButton(target, onSuccess, onError) {
       var elm;

       if (typeof target === 'string') {
           elm = document.querySelector(target);
       } else {
           elm = target;
       }

       var click = function () {
           try {
               var text = elm.dataset.clipboardText;
               copyText(text);
               if (onSuccess) {
                   onSuccess();
               }
           } catch (err) {
               if (onError) {
                   onError({err: err});
               }
           }
       };

       elm.addEventListener('click', click);

       return {
           destroy: function () {
               elm.removeEventListener('click', click);
           },
           element: elm
       };
   };

   clipboardButton.supported = 'queryCommandSupported' in document && document.queryCommandSupported('copy');

   return clipboardButton;

}));
