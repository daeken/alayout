ALayout -- Intelligent DSL for Android UIs
==========================================

ALayout is intended to be a simple, intelligent DSL for building Android UIs.
In its current form, it is really just a nicer syntax around the XML, but
future versions will have constants where useful, 'macros' for defining common
element groups, etc.

Example
-------

Here's some example XML from the Android SDK:

    <?xml version="1.0" encoding="utf-8"?>
    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
                  android:layout_width="fill_parent" 
                  android:layout_height="fill_parent" 
                  android:orientation="vertical" >
        <TextView android:id="@+id/text"
                  android:layout_width="wrap_content"
                  android:layout_height="wrap_content"
                  android:text="Hello, I am a TextView" />
        <Button android:id="@+id/button"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Hello, I am a Button" />
    </LinearLayout>

Now the equivalent ALayout code:

	from alayout import *
	
	with LinearLayout(width=FILL, height=FILL, orientation=VERTICAL):
		with TextView(id='text', width=WRAP, height=WRAP) as tv:
			tv['text'] = 'Hello, I am a TextView'
		Button(
				id='button', width=WRAP, height=WRAP,
				text='Hello, I am a Button'
			)

There's a lot less repetition, and you have the ability to write it how you wish.
You should use `with` blocks for nesting, but you can also use them for
non-nested tags, as you can see with the `TextView`.  You can also see how you
can modify attributes on tags after creation.  Note that some attributes are
special: id has its value transformed to prepend `@+id/`, `width/height` become
`layout_width/height`, etc.

Running
-------

Simply run the Python file containing your ALayout code, and it'll print your XML.
